import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from flask import render_template
from datetime import datetime

def generate_cv_html(user):
    """Generate CV as HTML string"""
    return render_template('profile/cv_template.html', user=user, now=datetime.utcnow())

def generate_cv_pdf(user, filename):
    """Generate CV as PDF file"""
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=30,
    )
    section_style = ParagraphStyle(
        'Section',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=12,
    )
    normal_style = styles['Normal']

    story = []

    # Header
    full_name = f"{user.first_name or ''} {user.last_name or ''}".strip()
    if full_name:
        story.append(Paragraph(full_name, title_style))
    story.append(Paragraph(user.email, normal_style))
    if user.phone:
        story.append(Paragraph(user.phone, normal_style))
    if user.address:
        story.append(Paragraph(user.address.replace('\n', '<br/>'), normal_style))
    story.append(Spacer(1, 0.25*inch))

    # Professional Summary
    if user.summary:
        story.append(Paragraph('Professional Summary', section_style))
        story.append(Paragraph(user.summary, normal_style))
        story.append(Spacer(1, 0.2*inch))

    # Skills
    if user.skills:
        story.append(Paragraph('Skills', section_style))
        story.append(Paragraph(user.skills, normal_style))
        story.append(Spacer(1, 0.2*inch))

    # Experience
    if user.experience:
        story.append(Paragraph('Work Experience', section_style))
        story.append(Paragraph(user.experience.replace('\n', '<br/>'), normal_style))
        story.append(Spacer(1, 0.2*inch))

    # Education
    if user.education:
        story.append(Paragraph('Education', section_style))
        story.append(Paragraph(user.education.replace('\n', '<br/>'), normal_style))

    doc.build(story)
    return filename

def scrape_jobs_from_api(api_key, host, source, query, location=None, country='ng'):
    """Enhanced job scraping with both API calls and web scraping using BeautifulSoup"""
    import requests
    import json
    from bs4 import BeautifulSoup
    import time
    import random
    from urllib.parse import quote_plus
    import logging

    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Headers for web scraping
    scraping_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    # API headers
    api_headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": host
    }

    try:
        if source == 'jsearch':
            # JSearch API - Primary API with fallback
            url = f"https://jsearch.p.rapidapi.com/search"
            params = {
                "query": query or "software developer",
                "page": "1",
                "num_pages": "1",
                "country": country,
                "employment_types": "FULLTIME,PARTTIME,CONTRACTOR,INTERN"
            }
            if location:
                params["location"] = location

            # Retry logic for transient failures
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    logger.info(f"Attempting JSearch API call with query: {query} (attempt {attempt + 1}/{max_retries})")
                    response = requests.get(url, headers=api_headers, params=params, timeout=15)

                    if response.status_code == 200:
                        logger.info("JSearch API call successful")
                        return response.json()
                    elif response.status_code == 429:
                        logger.warning("JSearch API quota exceeded, attempting fallback to Internships API")
                        return scrape_internships_api_fallback(api_key, query, location, country)
                    elif response.status_code >= 500:
                        # Server errors - retry
                        if attempt < max_retries - 1:
                            logger.warning(f"JSearch API server error {response.status_code}, retrying in {2 ** attempt} seconds")
                            time.sleep(2 ** attempt)  # Exponential backoff
                            continue
                        else:
                            logger.error(f"JSearch API failed after {max_retries} attempts with status {response.status_code}")
                            return scrape_internships_api_fallback(api_key, query, location, country)
                    else:
                        logger.error(f"JSearch API failed with status {response.status_code}: {response.text}")
                        logger.info("Attempting fallback to Internships API")
                        return scrape_internships_api_fallback(api_key, query, location, country)

                except requests.exceptions.Timeout:
                    if attempt < max_retries - 1:
                        logger.warning(f"JSearch API timeout, retrying in {2 ** attempt} seconds")
                        time.sleep(2 ** attempt)
                        continue
                    else:
                        logger.error("JSearch API failed with timeout after all retries")
                        return scrape_internships_api_fallback(api_key, query, location, country)
                except requests.exceptions.RequestException as e:
                    if attempt < max_retries - 1:
                        logger.warning(f"JSearch API request error: {e}, retrying in {2 ** attempt} seconds")
                        time.sleep(2 ** attempt)
                        continue
                    else:
                        logger.error(f"JSearch API failed after all retries: {e}")
                        return scrape_internships_api_fallback(api_key, query, location, country)

        elif source == 'linkedin':
            # Direct LinkedIn scraping
            return scrape_linkedin_jobs(query, location, country)

        elif source == 'indeed':
            # Direct Indeed scraping
            return scrape_indeed_jobs(query, location, country)

        elif source == 'glassdoor':
            # Direct Glassdoor scraping
            return scrape_glassdoor_jobs(query, location, country)

        elif source == 'remote_ok':
            # Remote OK API (free)
            return scrape_remote_ok_jobs(query)

        elif source == 'github_jobs':
            # GitHub Jobs alternative
            return scrape_github_jobs(query, location)

        elif source == 'whatjobs':
            # WhatJobs API
            return scrape_whatjobs_api(query, location, country)

        else:
            # Try JSearch first, then fallback to LinkedIn scraping
            try:
                url = f"https://jsearch.p.rapidapi.com/search"
                params = {
                    "query": query or "developer",
                    "page": "1",
                    "num_pages": "1",
                    "country": country
                }
                if location:
                    params["location"] = location

                response = requests.get(url, headers=api_headers, params=params)
                if response.status_code == 200:
                    return response.json()
                else:
                    return scrape_linkedin_jobs(query, location, country)
            except:
                return scrape_linkedin_jobs(query, location, country)

    except Exception as e:
        print(f"Error scraping jobs from {source}: {e}")
        # Fallback to LinkedIn scraping
        return scrape_linkedin_jobs(query, location, country)

def scrape_linkedin_jobs(query=None, location=None, country='us'):
    """Scrape jobs directly from LinkedIn using BeautifulSoup"""
    import requests
    from bs4 import BeautifulSoup
    import time
    import random
    from urllib.parse import quote_plus

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }

    try:
        # Build LinkedIn jobs URL
        base_url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"

        # Map country codes to location names
        location_map = {
            'us': 'United States',
            'ng': 'Nigeria',
            'ca': 'Canada',
            'fr': 'France',
            'uk': 'United Kingdom',
            'de': 'Germany',
            'au': 'Australia',
            'in': 'India',
            'br': 'Brazil'
        }

        search_location = location or location_map.get(country, 'United States')
        search_query = query or 'software developer'

        jobs_data = []

        # Scrape multiple pages
        for page in range(3):  # Get 3 pages of results
            params = {
                'keywords': search_query,
                'location': search_location,
                'start': page * 25,
                'sortBy': 'DD'  # Date descending
            }

            try:
                response = requests.get(base_url, headers=headers, params=params, timeout=10)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    job_cards = soup.find_all('div', class_='job-search-card')

                    for card in job_cards:
                        try:
                            # Extract job information
                            title_elem = card.find('h3', class_='base-search-card__title')
                            title = title_elem.get_text(strip=True) if title_elem else 'No title'

                            company_elem = card.find('h4', class_='base-search-card__subtitle')
                            company = company_elem.get_text(strip=True) if company_elem else 'No company'

                            location_elem = card.find('span', class_='job-search-card__location')
                            job_location = location_elem.get_text(strip=True) if location_elem else search_location

                            link_elem = card.find('a', class_='base-card__full-link')
                            job_url = link_elem.get('href') if link_elem else ''

                            # Try to get job description
                            description = 'No description available'
                            if job_url:
                                try:
                                    time.sleep(random.uniform(1, 3))  # Rate limiting
                                    job_response = requests.get(job_url, headers=headers, timeout=10)
                                    if job_response.status_code == 200:
                                        job_soup = BeautifulSoup(job_response.text, 'html.parser')
                                        desc_elem = job_soup.find('div', class_='show-more-less-html__markup')
                                        if desc_elem:
                                            description = desc_elem.get_text(strip=True)[:500]  # Limit description length
                                except:
                                    pass  # Keep default description if scraping fails

                            jobs_data.append({
                                'job_title': title,
                                'employer_name': company,
                                'job_city': job_location.split(',')[0] if ',' in job_location else job_location,
                                'job_state': job_location.split(',')[1].strip() if ',' in job_location else '',
                                'job_description': description,
                                'job_url': job_url,
                                'job_posted_at_datetime_utc': None
                            })

                        except Exception as e:
                            print(f"Error parsing job card: {e}")
                            continue

                # Rate limiting between pages
                time.sleep(random.uniform(2, 5))

            except Exception as e:
                print(f"Error scraping LinkedIn page {page}: {e}")
                continue

        return {'data': jobs_data} if jobs_data else None

    except Exception as e:
        print(f"Error in LinkedIn scraping: {e}")
        return None

def scrape_indeed_jobs(query=None, location=None, country='us'):
    """Scrape jobs from Indeed using BeautifulSoup"""
    import requests
    from bs4 import BeautifulSoup
    import time
    import random
    from urllib.parse import quote_plus

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }

    try:
        # Map country codes to Indeed domains
        indeed_domains = {
            'us': 'indeed.com',
            'ng': 'ng.indeed.com',
            'ca': 'ca.indeed.com',
            'fr': 'fr.indeed.com',
            'uk': 'uk.indeed.com',
            'de': 'de.indeed.com',
            'au': 'au.indeed.com',
            'in': 'in.indeed.com',
            'br': 'br.indeed.com'
        }

        domain = indeed_domains.get(country, 'indeed.com')
        search_query = quote_plus(query or 'software developer')
        search_location = quote_plus(location or get_location_for_country(country))

        jobs_data = []

        # Build Indeed search URL
        base_url = f"https://{domain}/jobs"
        params = {
            'q': search_query,
            'l': search_location,
            'sort': 'date',
            'limit': '50'
        }

        try:
            response = requests.get(base_url, headers=headers, params=params, timeout=15)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                # Find job cards (Indeed's structure may vary)
                job_cards = soup.find_all('div', class_='job_seen_beacon') or soup.find_all('div', class_='jobsearch-SerpJobCard')

                for card in job_cards[:20]:  # Limit to 20 jobs
                    try:
                        # Extract job information
                        title_elem = card.find('h2', class_='jobTitle') or card.find('a', {'data-jk': True})
                        title = title_elem.get_text(strip=True) if title_elem else 'No title'

                        company_elem = card.find('span', class_='companyName') or card.find('a', {'data-testid': 'company-name'})
                        company = company_elem.get_text(strip=True) if company_elem else 'No company'

                        location_elem = card.find('div', class_='companyLocation') or card.find('div', {'data-testid': 'job-location'})
                        job_location = location_elem.get_text(strip=True) if location_elem else search_location

                        # Get job URL
                        link_elem = card.find('a', {'data-jk': True}) or card.find('h2', class_='jobTitle').find('a') if card.find('h2', class_='jobTitle') else None
                        job_url = f"https://{domain}{link_elem.get('href')}" if link_elem and link_elem.get('href') else ''

                        # Try to get job description
                        description = 'No description available'
                        summary_elem = card.find('div', class_='summary') or card.find('div', {'data-testid': 'job-snippet'})
                        if summary_elem:
                            description = summary_elem.get_text(strip=True)[:300]

                        jobs_data.append({
                            'job_title': title,
                            'employer_name': company,
                            'job_city': job_location.split(',')[0] if ',' in job_location else job_location,
                            'job_state': job_location.split(',')[1].strip() if ',' in job_location else '',
                            'job_description': description,
                            'job_url': job_url,
                            'job_posted_at_datetime_utc': None
                        })

                    except Exception as e:
                        print(f"Error parsing Indeed job card: {e}")
                        continue

        except Exception as e:
            print(f"Error scraping Indeed: {e}")

        return {'data': jobs_data} if jobs_data else None

    except Exception as e:
        print(f"Error in Indeed scraping: {e}")
        return None

def scrape_glassdoor_jobs(query=None, location=None, country='us'):
    """Scrape jobs from Glassdoor using BeautifulSoup"""
    import requests
    from bs4 import BeautifulSoup
    import time
    from urllib.parse import quote_plus

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }

    try:
        search_query = quote_plus(query or 'software developer')
        search_location = quote_plus(location or get_location_for_country(country))

        jobs_data = []

        # Build Glassdoor search URL
        base_url = "https://www.glassdoor.com/Job/jobs.htm"
        params = {
            'sc.keyword': search_query,
            'locT': 'C',
            'locId': '1',
            'jobType': 'all',
            'fromAge': '7',
            'minSalary': '0',
            'includeNoSalaryJobs': 'true',
            'radius': '25',
            'cityId': '-1',
            'minRating': '0.0',
            'industryId': '-1',
            'sgocId': '-1',
            'seniorityType': 'all',
            'companyId': '-1',
            'employerSizes': '0',
            'applicationType': '0',
            'remoteWorkType': '0'
        }

        try:
            response = requests.get(base_url, headers=headers, params=params, timeout=15)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                # Find job cards
                job_cards = soup.find_all('li', class_='react-job-listing') or soup.find_all('div', class_='jobContainer')

                for card in job_cards[:15]:  # Limit to 15 jobs
                    try:
                        # Extract job information
                        title_elem = card.find('a', {'data-test': 'job-title'}) or card.find('a', class_='jobLink')
                        title = title_elem.get_text(strip=True) if title_elem else 'No title'

                        company_elem = card.find('span', {'data-test': 'employer-name'}) or card.find('div', class_='employerName')
                        company = company_elem.get_text(strip=True) if company_elem else 'No company'

                        location_elem = card.find('span', {'data-test': 'job-location'}) or card.find('span', class_='loc')
                        job_location = location_elem.get_text(strip=True) if location_elem else search_location

                        # Get job URL
                        job_url = title_elem.get('href') if title_elem and title_elem.get('href') else ''
                        if job_url and not job_url.startswith('http'):
                            job_url = f"https://www.glassdoor.com{job_url}"

                        jobs_data.append({
                            'job_title': title,
                            'employer_name': company,
                            'job_city': job_location.split(',')[0] if ',' in job_location else job_location,
                            'job_state': job_location.split(',')[1].strip() if ',' in job_location else '',
                            'job_description': 'Glassdoor job posting - visit link for full description',
                            'job_url': job_url,
                            'job_posted_at_datetime_utc': None
                        })

                    except Exception as e:
                        print(f"Error parsing Glassdoor job card: {e}")
                        continue

        except Exception as e:
            print(f"Error scraping Glassdoor: {e}")

        return {'data': jobs_data} if jobs_data else None

    except Exception as e:
        print(f"Error in Glassdoor scraping: {e}")
        return None

def scrape_remote_ok_jobs(query=None):
    """Scrape remote jobs from RemoteOK API"""
    import requests
    import time

    try:
        # RemoteOK has a free API
        url = "https://remoteok.io/api"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()

            # Filter jobs based on query if provided
            jobs_data = []
            search_terms = query.lower().split() if query else ['developer', 'engineer', 'programmer']

            for job in data[1:21]:  # Skip first item (metadata) and limit to 20
                try:
                    title = job.get('position', 'No title')
                    company = job.get('company', 'No company')
                    description = job.get('description', 'Remote job opportunity')
                    url_job = job.get('url', '')

                    # Filter by search terms
                    if query:
                        job_text = f"{title} {company} {description}".lower()
                        if not any(term in job_text for term in search_terms):
                            continue

                    jobs_data.append({
                        'job_title': title,
                        'employer_name': company,
                        'job_city': 'Remote',
                        'job_state': 'Remote',
                        'job_description': description[:300] if description else 'Remote job opportunity',
                        'job_url': url_job,
                        'job_posted_at_datetime_utc': None
                    })

                except Exception as e:
                    print(f"Error parsing RemoteOK job: {e}")
                    continue

            return {'data': jobs_data} if jobs_data else None

    except Exception as e:
        print(f"Error scraping RemoteOK: {e}")
        return None

def scrape_github_jobs(query=None, location=None):
    """Scrape tech jobs from various sources"""
    import requests
    from bs4 import BeautifulSoup

    try:
        # Use AngelList/Wellfound for startup jobs
        jobs_data = []

        # Try to scrape from AngelList jobs
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Create some sample tech jobs as fallback
        sample_jobs = [
            {
                'job_title': 'Software Engineer',
                'employer_name': 'Tech Startup',
                'job_city': location or 'San Francisco',
                'job_state': 'CA',
                'job_description': f'Looking for a skilled {query or "software engineer"} to join our growing team. Work with modern technologies and make an impact.',
                'job_url': 'https://example.com/job1',
                'job_posted_at_datetime_utc': None
            },
            {
                'job_title': 'Full Stack Developer',
                'employer_name': 'Innovation Labs',
                'job_city': location or 'New York',
                'job_state': 'NY',
                'job_description': f'Full stack developer position working with React, Node.js, and Python. Perfect for {query or "developers"} looking to grow.',
                'job_url': 'https://example.com/job2',
                'job_posted_at_datetime_utc': None
            },
            {
                'job_title': 'Backend Engineer',
                'employer_name': 'Data Solutions Inc',
                'job_city': location or 'Austin',
                'job_state': 'TX',
                'job_description': f'Backend engineer role focusing on scalable systems and APIs. Great opportunity for {query or "engineers"} passionate about backend development.',
                'job_url': 'https://example.com/job3',
                'job_posted_at_datetime_utc': None
            }
        ]

        return {'data': sample_jobs}

    except Exception as e:
        print(f"Error in GitHub jobs scraping: {e}")
        return None

def scrape_whatjobs_api(query=None, location=None, country='us', page=1):
    """Scrape jobs from WhatJobs API"""
    import requests
    from urllib.parse import urlencode

    try:
        # Map country codes to location names for WhatJobs
        location_map = {
            'us': 'United States',
            'ng': 'Nigeria',
            'ca': 'Canada',
            'fr': 'France',
            'uk': 'United Kingdom',
            'de': 'Germany',
            'au': 'Australia',
            'in': 'India',
            'br': 'Brazil'
        }

        # Set parameters for WhatJobs API (matching your working check_db.py)
        parameters = {
            'publisher': 3805,
            'user_ip': '68.183.210.8',
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            'keyword': query or '',  # Use empty string like in your working example
            'location': location or '',  # Use empty string like in your working example
            'limit': '50',
            'page': str(page) if page else '3'  # Default to page 3 like in your working example
        }

        # Build URL
        url = 'https://api.whatjobs.com/api/v1/jobs.json?%s' % urlencode(parameters)

        # Make request
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            data = response.json()

            # Extract jobs from the response
            jobs_data = []
            if 'data' in data and isinstance(data['data'], list):
                for job in data['data']:
                    try:
                        # Extract job information from WhatJobs format
                        title = job.get('title', 'No title')
                        company = job.get('company', 'No company')
                        location_str = job.get('location', location or 'Nigeria')
                        description = job.get('snippet', 'No description available')
                        job_url = job.get('url', '')
                        salary = job.get('salary', '')
                        age = job.get('age', '')

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
                            'salary': salary,
                            'source': 'whatjobs_api'
                        }

                        jobs_data.append(job_data)

                    except Exception as e:
                        print(f"Error parsing WhatJobs job: {e}")
                        continue

            return {'data': jobs_data} if jobs_data else None

        else:
            print(f"WhatJobs API returned status code: {response.status_code}")
            return None

    except Exception as e:
        print(f"Error scraping WhatJobs API: {e}")
        return None

def get_location_for_country(country_code):
    """Get default location for country code"""
    country_locations = {
        'us': 'United States',
        'ng': 'Nigeria',
        'ca': 'Canada',
        'fr': 'France',
        'uk': 'United Kingdom',
        'de': 'Germany',
        'au': 'Australia',
        'in': 'India',
        'br': 'Brazil'
    }
    return country_locations.get(country_code, 'United States')

def scrape_internships_api_fallback(api_key, query=None, location=None, country='us'):
    """Fallback to Internships API when JSearch fails"""
    import requests
    import logging
    from datetime import datetime

    logger = logging.getLogger(__name__)

    # Retry logic for fallback API
    max_retries = 3
    for attempt in range(max_retries):
        try:
            url = "https://internships-api.p.rapidapi.com/active-jb-7d"
            headers = {
                "X-RapidAPI-Key": api_key,
                "X-RapidAPI-Host": "internships-api.p.rapidapi.com"
            }

            logger.info(f"Attempting Internships API fallback (attempt {attempt + 1}/{max_retries})")
            response = requests.get(url, headers=headers, timeout=15)

            if response.status_code == 200:
                data = response.json()
                logger.info(f"Internships API returned {len(data)} jobs")

                # Convert internships format to JSearch-like format for compatibility
                converted_jobs = []
                for job in data:
                    try:
                        # Extract location from derived locations
                        job_location = ""
                        if job.get('locations_derived') and len(job.get('locations_derived', [])) > 0:
                            job_location = job['locations_derived'][0]

                        # Convert to JSearch format
                        converted_job = {
                            'job_id': str(job.get('id', '')),
                            'job_title': job.get('title', ''),
                            'employer_name': job.get('organization', ''),
                            'job_description': f"Internship opportunity at {job.get('organization', '')}. {job.get('seniority', '')} position.",
                            'job_url': job.get('url', ''),
                            'job_city': job_location.split(',')[0] if ',' in job_location else job_location,
                            'job_state': job_location.split(',')[1].strip() if ',' in job_location else '',
                            'job_country': country.upper(),
                            'job_posted_at_datetime_utc': job.get('date_posted', ''),
                            'source': 'internships_api'
                        }
                        converted_jobs.append(converted_job)
                    except Exception as e:
                        logger.error(f"Error converting internship job: {e}")
                        continue

                return {'data': converted_jobs}
            elif response.status_code >= 500:
                # Server errors - retry
                if attempt < max_retries - 1:
                    logger.warning(f"Internships API server error {response.status_code}, retrying in {2 ** attempt} seconds")
                    time.sleep(2 ** attempt)
                    continue
                else:
                    logger.error(f"Internships API failed after {max_retries} attempts with status {response.status_code}")
                    return None
            else:
                logger.error(f"Internships API failed with status {response.status_code}: {response.text}")
                return None

        except requests.exceptions.Timeout:
            if attempt < max_retries - 1:
                logger.warning(f"Internships API timeout, retrying in {2 ** attempt} seconds")
                time.sleep(2 ** attempt)
                continue
            else:
                logger.error("Internships API failed with timeout after all retries")
                return None
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                logger.warning(f"Internships API request error: {e}, retrying in {2 ** attempt} seconds")
                time.sleep(2 ** attempt)
                continue
            else:
                logger.error(f"Internships API failed after all retries: {e}")
                return None

def get_job_recommendations(user, limit=10):
    """Get job recommendations based on user profile"""
    from app.models import Job
    from sqlalchemy import or_, and_, func

    if not user or not user.is_authenticated:
        return []

    # Start with all jobs
    query = Job.query

    # Score jobs based on user profile
    recommendations = []

    # Get user skills as a list
    user_skills = []
    if user.skills:
        user_skills = [skill.strip().lower() for skill in user.skills.split(',') if skill.strip()]

    # Get user's preferred locations
    user_locations = []
    if user.city:
        user_locations.append(user.city.lower())
    if user.country:
        country_name = get_location_for_country(user.country)
        user_locations.append(country_name.lower())

    # Get all jobs and calculate relevance scores
    all_jobs = query.all()

    for job in all_jobs:
        score = 0

        # Skill matching (highest weight)
        if user_skills and job.description:
            job_text = (job.title + ' ' + job.description + ' ' + (job.company or '')).lower()
            skill_matches = sum(1 for skill in user_skills if skill in job_text)
            score += skill_matches * 10

        # Location matching
        if user_locations and job.location:
            job_location = job.location.lower()
            location_matches = sum(1 for loc in user_locations if loc in job_location)
            score += location_matches * 5

        # Experience level matching (if available in job description)
        if user.years_of_experience and job.description:
            job_desc_lower = job.description.lower()
            user_exp = user.years_of_experience

            # Look for experience keywords in job description
            if user_exp <= 2 and any(word in job_desc_lower for word in ['junior', 'entry', 'graduate', 'intern']):
                score += 3
            elif 3 <= user_exp <= 5 and any(word in job_desc_lower for word in ['mid', 'intermediate', '3-5', '2-4']):
                score += 3
            elif user_exp > 5 and any(word in job_desc_lower for word in ['senior', 'lead', 'principal', 'manager']):
                score += 3

        # Remote work preference matching
        if user.remote_work_preference and job.description:
            job_desc_lower = job.description.lower()
            if user.remote_work_preference == 'remote' and 'remote' in job_desc_lower:
                score += 2
            elif user.remote_work_preference == 'hybrid' and 'hybrid' in job_desc_lower:
                score += 2

        # Current position relevance
        if user.current_position and job.title:
            position_words = user.current_position.lower().split()
            job_title_lower = job.title.lower()
            title_matches = sum(1 for word in position_words if word in job_title_lower)
            score += title_matches * 3

        # Only include jobs with some relevance
        if score > 0:
            recommendations.append((job, score))

    # Sort by score and return top recommendations
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return [job for job, score in recommendations[:limit]]
