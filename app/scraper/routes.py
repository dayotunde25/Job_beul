from flask import render_template, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from functools import wraps
from __init__ import db
from app.scraper import bp
from app.forms import ScraperForm
from app.models import Job
from app.utils import scrape_jobs_from_api
from datetime import datetime

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Admin access required to use the scraper.', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

def extract_job_fields(job_data, source):
    """Extract job fields from API response based on source"""
    if source == 'jsearch':
        title = job_data.get('job_title', '')
        company = job_data.get('employer_name', '')
        location = f"{job_data.get('job_city', '')}, {job_data.get('job_state', '')}".strip(', ')
        description = job_data.get('job_description', '')
        url = job_data.get('job_url', '')
        date_posted_str = job_data.get('job_posted_at_datetime_utc', '')
        date_posted = datetime.fromisoformat(date_posted_str.replace('Z', '+00:00')) if date_posted_str else None

    elif source == 'internships_api':
        # Handle internships API format (fallback)
        title = job_data.get('job_title', '')
        company = job_data.get('employer_name', '')
        location = f"{job_data.get('job_city', '')}, {job_data.get('job_state', '')}".strip(', ')
        description = job_data.get('job_description', '')
        url = job_data.get('job_url', '')
        date_posted_str = job_data.get('job_posted_at_datetime_utc', '')
        date_posted = datetime.fromisoformat(date_posted_str.replace('Z', '+00:00')) if date_posted_str else None

    elif source in ['linkedin', 'indeed']:
        title = job_data.get('title', '') or job_data.get('job_title', '')
        company = job_data.get('company', '') or job_data.get('company_name', '')
        location = job_data.get('location', '') or job_data.get('job_location', '')
        description = job_data.get('description', '') or job_data.get('job_description', '')
        url = job_data.get('url', '') or job_data.get('job_url', '') or job_data.get('link', '')
        date_posted = None

    elif source == 'latest-jobs':
        title = job_data.get('title', '') or job_data.get('job_title', '')
        company = job_data.get('company', '') or job_data.get('company_name', '')
        location = job_data.get('location', '') or job_data.get('job_location', '')
        description = job_data.get('description', '') or job_data.get('job_description', '')
        url = job_data.get('url', '') or job_data.get('job_url', '') or job_data.get('link', '')
        date_posted_str = job_data.get('datePosted', '') or job_data.get('date_posted', '')
        date_posted = datetime.fromisoformat(date_posted_str.replace('Z', '+00:00')) if date_posted_str else None

    elif source == 'jobicy':
        title = job_data.get('jobTitle', '') or job_data.get('title', '')
        company = job_data.get('companyName', '') or job_data.get('company', '')
        location = job_data.get('jobGeo', '') or job_data.get('location', '')
        description = job_data.get('jobDescription', '') or job_data.get('description', '')
        url = job_data.get('url', '') or job_data.get('job_url', '')
        date_posted_str = job_data.get('pubDate', '') or job_data.get('date_posted', '')
        date_posted = datetime.fromisoformat(date_posted_str.replace('Z', '+00:00')) if date_posted_str else None

    else:
        # Generic extraction for other APIs
        title = (job_data.get('title') or job_data.get('job_title') or
                job_data.get('position') or job_data.get('name', ''))
        company = (job_data.get('company') or job_data.get('company_name') or
                  job_data.get('employer') or job_data.get('employer_name', ''))
        location = (job_data.get('location') or job_data.get('job_location') or
                   job_data.get('city') or job_data.get('address', ''))
        description = (job_data.get('description') or job_data.get('job_description') or
                      job_data.get('summary') or job_data.get('details', ''))
        url = (job_data.get('url') or job_data.get('job_url') or
              job_data.get('link') or job_data.get('apply_url', ''))
        date_posted = None

    return title, company, location, description, url, date_posted

@bp.route('/scrape', methods=['GET', 'POST'])
@login_required
@admin_required
def scrape():
    form = ScraperForm()
    if form.validate_on_submit():
        api_key = current_app.config.get('RAPIDAPI_KEY')
        if not api_key:
            flash('RapidAPI key not configured', 'danger')
            return redirect(url_for('scraper.scrape'))

        # Determine API host based on source
        api_hosts = {
            'jsearch': 'jsearch.p.rapidapi.com',
            'linkedin': 'linkedin-jobs-search.p.rapidapi.com',
            'indeed': 'indeed12.p.rapidapi.com',
            'latest-jobs': 'latest-jobs.p.rapidapi.com',
            'jobicy': 'jobicy.p.rapidapi.com',
            'jobs-api': 'jobs-api19.p.rapidapi.com',
            'greenhouse': 'greenhouse-job-board.p.rapidapi.com',
            'jooble': 'jooble-job-search.p.rapidapi.com',
            'gupy': 'gupy-jobs.p.rapidapi.com',
            'jobvacancies': 'job-vacancies.p.rapidapi.com',
            'whatsjob': 'whatsjob.p.rapidapi.com'
        }

        host = api_hosts.get(form.source.data, current_app.config.get('RAPIDAPI_HOST', 'jsearch.p.rapidapi.com'))

        # Make query, location, country optional by passing None if empty
        query = form.query.data if form.query.data else None
        location = form.location.data if form.location.data else None
        country = form.country.data if form.country.data else None

        jobs_data = scrape_jobs_from_api(
            api_key, host, form.source.data,
            query, location, country
        )

        if jobs_data:
            jobs_added = 0

            # Handle different response structures
            if isinstance(jobs_data, list):
                job_list = jobs_data
            elif isinstance(jobs_data, dict):
                if 'data' in jobs_data:
                    job_list = jobs_data['data'] if isinstance(jobs_data['data'], list) else [jobs_data['data']]
                elif 'jobs' in jobs_data:
                    job_list = jobs_data['jobs'] if isinstance(jobs_data['jobs'], list) else [jobs_data['jobs']]
                else:
                    job_list = [jobs_data]
            else:
                job_list = []

            for job_data in job_list:
                if not job_data or not isinstance(job_data, dict):
                    continue

                # Extract job URL for duplicate checking
                job_url = (job_data.get('job_url') or job_data.get('url') or
                          job_data.get('link') or job_data.get('apply_url') or '')

                if not job_url:
                    continue

                # Check if job URL already exists
                existing_job = Job.query.filter_by(url=job_url).first()
                if existing_job:
                    continue

                # Extract job data based on API source with improved field mapping
                title, company, location, description, url, date_posted = extract_job_fields(job_data, form.source.data)

                # Skip if essential fields are missing
                if not title or not url:
                    continue

                # Use the source from job data if available (for fallback APIs), otherwise use form source
                job_source = job_data.get('source', form.source.data)

                job = Job(
                    title=title,
                    company=company,
                    location=location,
                    description=description,
                    url=url,
                    date_posted=date_posted,
                    source=job_source
                )
                db.session.add(job)
                jobs_added += 1

            db.session.commit()
            flash(f'Successfully added {jobs_added} new jobs from {form.source.data}!', 'success')
        else:
            flash(f'Failed to fetch jobs from {form.source.data} API', 'danger')

        return redirect(url_for('main.index'))

    return render_template('scraper/scrape.html', title='Scrape Jobs', form=form)
