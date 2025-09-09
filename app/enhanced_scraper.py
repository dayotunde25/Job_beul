#!/usr/bin/env python3
"""
Enhanced job scraping module with BeautifulSoup and multiple sources
Implements the LinkedIn scraping approach shown in the user's code
Now with real-time database insertion for each page scraped
"""

import requests
from bs4 import BeautifulSoup
import time
import random
import json
from datetime import datetime
from urllib.parse import quote_plus, urljoin
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class JobScraper:
    def __init__(self, save_to_db=True):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        self.save_to_db = save_to_db
        self.total_jobs_saved = 0
        
    def delay(self, min_seconds=3, max_seconds=5):
        """Add random delay to avoid being blocked"""
        time.sleep(random.uniform(min_seconds, max_seconds))

    def save_jobs_to_database(self, jobs_data, source_name):
        """Save jobs to database immediately"""
        if not self.save_to_db or not jobs_data:
            return 0

        try:
            # Import here to avoid circular imports
            from app.models import Job
            from flask import current_app

            # Ensure we're in Flask app context
            if not current_app:
                logger.error("No Flask app context available for database operations")
                return 0

            from __init__ import db

            jobs_saved = 0

            for job_data in jobs_data:
                try:
                    # Check if job URL already exists
                    job_url = job_data.get('job_url', '')
                    if not job_url:
                        continue

                    existing_job = Job.query.filter_by(url=job_url).first()
                    if existing_job:
                        logger.debug(f"Job already exists: {job_data.get('job_title', 'Unknown')}")
                        continue

                    # Skip if essential fields are missing
                    if not job_data.get('job_title'):
                        continue

                    # Handle location - use country if location not available
                    location = f"{job_data.get('job_city', '')}, {job_data.get('job_state', '')}".strip(', ')
                    if not location or location == ',':
                        location = job_data.get('country', 'Remote')

                    # Handle date - use current date if not available
                    from datetime import datetime
                    date_posted = job_data.get('job_posted_at_datetime_utc')
                    if not date_posted:
                        date_posted = datetime.utcnow()

                    # Create new job
                    job = Job(
                        title=job_data.get('job_title', ''),
                        company=job_data.get('employer_name', ''),
                        location=location,
                        description=job_data.get('job_description', '')[:1000],  # Limit description
                        url=job_url,
                        date_posted=date_posted,
                        source=job_data.get('source', source_name)
                    )

                    db.session.add(job)
                    jobs_saved += 1
                    logger.debug(f"Added job to session: {job.title} at {job.company}")

                except Exception as e:
                    logger.error(f"Error processing individual job: {e}")
                    continue

            # Commit the batch
            if jobs_saved > 0:
                db.session.commit()
                self.total_jobs_saved += jobs_saved
                logger.info(f"✅ Saved {jobs_saved} new jobs from {source_name} to database")
            else:
                logger.info(f"ℹ️  No new jobs to save from {source_name} (all were duplicates or invalid)")

            return jobs_saved

        except Exception as e:
            logger.error(f"Error saving jobs to database: {e}")
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}")
            try:
                db.session.rollback()
            except:
                pass
            return 0
    
    def scrape_linkedin_jobs(self, countries=None, query=""):
        """
        Scrape LinkedIn jobs similar to the JavaScript approach shown
        """
        if countries is None:
            countries = ['Nigeria', 'USA', 'France', 'Ghana', 'UK', 'Sweden', 'Canada', 'India', 'Brazil', 'Australia', 'Egypt', 'Liberia']
        
        all_jobs = []
        
        for country in countries:
            logger.info(f"Scraping jobs for {country}")
            
            try:
                # Scrape multiple pages for each country
                for page in range(5):  # 5 pages like in the JS code
                    start = page * 10
                    
                    # Build LinkedIn URL similar to the JavaScript version
                    url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
                    params = {
                        'location': country,
                        'keywords': query,
                        'trk': 'public_jobs_jobs-search-bar_search-submit',
                        'position': '1',
                        'pageNum': '0',
                        'start': str(start)
                    }
                    
                    try:
                        response = self.session.get(url, params=params, timeout=15)
                        if response.status_code == 200:
                            # Parse the HTML response
                            soup = BeautifulSoup(response.text, 'html.parser')
                            jobs = self.parse_linkedin_jobs(soup, country)

                            # Save jobs to database immediately
                            if jobs:
                                saved_count = self.save_jobs_to_database(jobs, 'linkedin_scraper')
                                logger.info(f"📄 Page {page + 1} for {country}: Found {len(jobs)} jobs, saved {saved_count} new jobs")
                            else:
                                logger.info(f"📄 Page {page + 1} for {country}: No jobs found")

                            all_jobs.extend(jobs)
                        else:
                            logger.warning(f"Failed to fetch LinkedIn jobs for {country}, page {page + 1}: {response.status_code}")
                            
                    except Exception as e:
                        logger.error(f"Error scraping LinkedIn page {page + 1} for {country}: {e}")
                        continue
                    
                    # Add delay between pages
                    self.delay(2, 5)
                
                # Add delay between countries
                self.delay(3, 6)
                
            except Exception as e:
                logger.error(f"Error scraping LinkedIn for {country}: {e}")
                continue
        
        return all_jobs
    
    def parse_linkedin_jobs(self, soup, country):
        """Parse LinkedIn job listings from BeautifulSoup object"""
        jobs = []
        
        # Find job cards in LinkedIn's structure
        job_cards = soup.find_all('div', class_='job-search-card') or soup.find_all('li', class_='result-card')
        
        for card in job_cards:
            try:
                # Extract job title
                title_elem = (card.find('h3', class_='base-search-card__title') or 
                             card.find('h3', class_='result-card__title') or
                             card.find('a', class_='result-card__full-card-link'))
                title = title_elem.get_text(strip=True) if title_elem else 'No title'
                
                # Extract company name
                company_elem = (card.find('h4', class_='base-search-card__subtitle') or
                               card.find('a', class_='result-card__subtitle-link') or
                               card.find('span', class_='result-card__subtitle'))
                company = company_elem.get_text(strip=True) if company_elem else 'No company'
                
                # Extract location
                location_elem = (card.find('span', class_='job-search-card__location') or
                                card.find('span', class_='result-card__location'))
                location = location_elem.get_text(strip=True) if location_elem else country
                
                # Extract job URL
                link_elem = (card.find('a', class_='base-card__full-link') or
                            card.find('a', class_='result-card__full-card-link'))
                job_url = link_elem.get('href') if link_elem else ''
                if job_url and not job_url.startswith('http'):
                    job_url = urljoin('https://www.linkedin.com', job_url)
                
                # Try to extract job description
                description = self.get_job_description(job_url) if job_url else 'No description available'
                
                job_data = {
                    'job_title': title,
                    'employer_name': company,
                    'job_city': location.split(',')[0] if ',' in location else location,
                    'job_state': location.split(',')[1].strip() if ',' in location else '',
                    'job_description': description,
                    'job_url': job_url,
                    'job_posted_at_datetime_utc': None,
                    'source': 'linkedin_scraper',
                    'country': country  # Add country for location fallback
                }
                
                jobs.append(job_data)
                
            except Exception as e:
                logger.error(f"Error parsing LinkedIn job card: {e}")
                continue
        
        return jobs
    
    def get_job_description(self, job_url):
        """Get detailed job description from job URL"""
        try:
            response = self.session.get(job_url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find job description in LinkedIn's structure
                desc_elem = (soup.find('div', class_='show-more-less-html__markup') or
                            soup.find('div', class_='description__text') or
                            soup.find('section', class_='description'))
                
                if desc_elem:
                    description = desc_elem.get_text(strip=True)
                    return description[:800]  # Limit description length
                    
        except Exception as e:
            logger.error(f"Error getting job description from {job_url}: {e}")
        
        return 'No description available'
    
    def scrape_indeed_jobs(self, countries=None, query="software developer"):
        """Scrape Indeed jobs for multiple countries"""
        if countries is None:
            countries = ['Nigeria', 'USA', 'France', 'Canada', 'UK', 'Australia', 'India']
        
        # Map countries to Indeed domains
        indeed_domains = {
            'Nigeria': 'ng.indeed.com',
            'USA': 'indeed.com',
            'France': 'fr.indeed.com',
            'Canada': 'ca.indeed.com',
            'UK': 'uk.indeed.com',
            'Australia': 'au.indeed.com',
            'India': 'in.indeed.com',
            'Germany': 'de.indeed.com',
            'Brazil': 'br.indeed.com'
        }
        
        all_jobs = []
        
        for country in countries:
            domain = indeed_domains.get(country, 'indeed.com')
            logger.info(f"Scraping Indeed jobs for {country} on {domain}")
            
            try:
                url = f"https://{domain}/jobs"
                params = {
                    'q': query,
                    'l': country,
                    'sort': 'date',
                    'limit': '50'
                }
                
                response = self.session.get(url, params=params, timeout=15)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    jobs = self.parse_indeed_jobs(soup, country)

                    # Save jobs to database immediately
                    if jobs:
                        saved_count = self.save_jobs_to_database(jobs, 'indeed_scraper')
                        logger.info(f"🌍 Indeed {country}: Found {len(jobs)} jobs, saved {saved_count} new jobs")
                    else:
                        logger.info(f"🌍 Indeed {country}: No jobs found")

                    all_jobs.extend(jobs)
                else:
                    logger.warning(f"Failed to fetch Indeed jobs for {country}: {response.status_code}")
                    
            except Exception as e:
                logger.error(f"Error scraping Indeed for {country}: {e}")
                continue
            
            # Add delay between countries
            self.delay(2, 4)
        
        return all_jobs
    
    def parse_indeed_jobs(self, soup, country):
        """Parse Indeed job listings"""
        jobs = []
        
        # Find job cards in Indeed's structure
        job_cards = (soup.find_all('div', class_='job_seen_beacon') or 
                    soup.find_all('div', class_='jobsearch-SerpJobCard') or
                    soup.find_all('a', {'data-jk': True}))
        
        for card in job_cards[:20]:  # Limit to 20 jobs per country
            try:
                # Extract job information
                title_elem = (card.find('h2', class_='jobTitle') or 
                             card.find('a', {'data-jk': True}) or
                             card.find('span', {'title': True}))
                title = title_elem.get('title') or title_elem.get_text(strip=True) if title_elem else 'No title'
                
                company_elem = (card.find('span', class_='companyName') or
                               card.find('a', {'data-testid': 'company-name'}))
                company = company_elem.get_text(strip=True) if company_elem else 'No company'
                
                location_elem = (card.find('div', class_='companyLocation') or
                                card.find('div', {'data-testid': 'job-location'}))
                location = location_elem.get_text(strip=True) if location_elem else country
                
                # Get job URL
                link_elem = card.find('a', {'data-jk': True}) or card.find('h2', class_='jobTitle').find('a') if card.find('h2', class_='jobTitle') else None
                job_url = f"https://indeed.com{link_elem.get('href')}" if link_elem and link_elem.get('href') else ''
                
                # Get job description
                summary_elem = (card.find('div', class_='summary') or
                               card.find('div', {'data-testid': 'job-snippet'}))
                description = summary_elem.get_text(strip=True)[:400] if summary_elem else 'No description available'
                
                job_data = {
                    'job_title': title,
                    'employer_name': company,
                    'job_city': location.split(',')[0] if ',' in location else location,
                    'job_state': location.split(',')[1].strip() if ',' in location else '',
                    'job_description': description,
                    'job_url': job_url,
                    'job_posted_at_datetime_utc': None,
                    'source': 'indeed_scraper',
                    'country': country  # Add country for location fallback
                }
                
                jobs.append(job_data)
                
            except Exception as e:
                logger.error(f"Error parsing Indeed job card: {e}")
                continue
        
        return jobs

    def scrape_whatjobs_api(self, countries=None, query="software developer"):
        """Scrape jobs from WhatJobs API for multiple countries"""
        if countries is None:
            countries = ['Nigeria', 'USA', 'France', 'Canada', 'UK', 'Australia', 'India']

        from urllib.parse import urlencode

        all_jobs = []

        for country in countries:
            logger.info(f"Scraping WhatJobs API for {country}")

            try:
                # Set parameters for WhatJobs API (matching working check_db.py)
                parameters = {
                    'publisher': 3805,
                    'user_ip': '68.183.210.8',
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
                    'keyword': '',  # Use empty string like in working example
                    'location': '',  # Use empty string like in working example
                    'limit': '50',
                    'page': '3'  # Use page 3 like in working example
                }

                # Build URL
                url = 'https://api.whatjobs.com/api/v1/jobs.json?%s' % urlencode(parameters)

                # Make request
                response = self.session.get(url, timeout=15)
                if response.status_code == 200:
                    data = response.json()

                    # Extract jobs from the response
                    country_jobs = []
                    if 'data' in data and isinstance(data['data'], list):
                        for job in data['data']:
                            try:
                                # Extract job information from WhatJobs format
                                title = job.get('title', 'No title')
                                company = job.get('company', 'No company')
                                location_str = job.get('location', country)
                                description = job.get('snippet', 'No description available')
                                job_url = job.get('url', '')

                                # Clean up description (remove escape characters)
                                if description:
                                    description = description.replace('\\r\\n', ' ').replace('\\n', ' ').replace('\\', '')
                                    description = description[:800]  # Limit description length

                                # Parse location
                                job_city = location_str.split(',')[0] if ',' in location_str else location_str
                                job_state = location_str.split(',')[1].strip() if ',' in location_str else ''

                                job_data = {
                                    'job_title': title,
                                    'employer_name': company,
                                    'job_city': job_city,
                                    'job_state': job_state,
                                    'job_description': description,
                                    'job_url': job_url,
                                    'job_posted_at_datetime_utc': None,
                                    'source': 'whatjobs_api',
                                    'country': country  # Add country for location fallback
                                }

                                country_jobs.append(job_data)

                            except Exception as e:
                                logger.error(f"Error parsing WhatJobs job: {e}")
                                continue

                    # Save jobs to database immediately
                    if country_jobs:
                        saved_count = self.save_jobs_to_database(country_jobs, 'whatjobs_api')
                        logger.info(f"🚀 WhatJobs {country}: Found {len(country_jobs)} jobs, saved {saved_count} new jobs")
                        all_jobs.extend(country_jobs)
                    else:
                        logger.info(f"🚀 WhatJobs {country}: No jobs found")

                else:
                    logger.warning(f"WhatJobs API returned status code: {response.status_code} for {country}")

            except Exception as e:
                logger.error(f"Error scraping WhatJobs for {country}: {e}")
                continue

            # Add delay between countries
            self.delay(2, 4)

        return all_jobs

def run_comprehensive_scraping():
    """Run comprehensive job scraping with real-time database insertion"""
    logger.info("🚀 Starting Comprehensive Job Scraping with Real-time Database Insertion")
    logger.info("=" * 80)

    scraper = JobScraper(save_to_db=True)

    # Countries to scrape (matching the JavaScript array)
    countries = ['Nigeria', 'USA', 'France', 'Ghana', 'UK', 'Sweden', 'Canada', 'India', 'Brazil', 'Australia', 'Egypt', 'Liberia']

    all_jobs = []

    # Scrape LinkedIn jobs
    logger.info("🔗 Starting LinkedIn job scraping...")
    logger.info("-" * 50)
    linkedin_jobs = scraper.scrape_linkedin_jobs(countries)
    all_jobs.extend(linkedin_jobs)
    logger.info(f"✅ LinkedIn scraping completed. Total jobs saved so far: {scraper.total_jobs_saved}")

    # Scrape Indeed jobs
    logger.info("\n🔍 Starting Indeed job scraping...")
    logger.info("-" * 50)
    indeed_jobs = scraper.scrape_indeed_jobs(countries)
    all_jobs.extend(indeed_jobs)
    logger.info(f"✅ Indeed scraping completed. Total jobs saved so far: {scraper.total_jobs_saved}")

    # Scrape WhatJobs API
    logger.info("\n🌟 Starting WhatJobs API scraping...")
    logger.info("-" * 50)
    whatjobs_jobs = scraper.scrape_whatjobs_api(countries)
    all_jobs.extend(whatjobs_jobs)
    logger.info(f"✅ WhatJobs scraping completed. Total jobs saved so far: {scraper.total_jobs_saved}")

    # Final summary
    logger.info("\n" + "=" * 80)
    logger.info(f"🎉 COMPREHENSIVE SCRAPING COMPLETED!")
    logger.info(f"📊 Total jobs found: {len(all_jobs)}")
    logger.info(f"💾 Total jobs saved to database: {scraper.total_jobs_saved}")
    logger.info(f"🌍 Countries scraped: {len(countries)}")
    logger.info(f"🔗 Sources used: LinkedIn, Indeed, WhatJobs API")
    logger.info("=" * 80)

    return all_jobs

if __name__ == "__main__":
    jobs = run_comprehensive_scraping()
    print(f"Scraped {len(jobs)} jobs total")
