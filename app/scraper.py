from flask import render_template, redirect, url_for, flash, current_app
from flask_login import login_required
from __init__ import db
from app.scraper import bp
from app.forms import ScraperForm
from app.models import Job
from app.utils import scrape_jobs_from_api
from datetime import datetime

@bp.route('/scrape', methods=['GET', 'POST'])
@login_required
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
            'greenhouse': 'https://company-jobs.p.rapidapi.com/greenhouse/nubank',
            'jooble': 'jooble-job-search.p.rapidapi.com',
            'gupy': 'gupy-jobs.p.rapidapi.com',
            'jobvacancies': 'job-vacancies.p.rapidapi.com',
            'whatsjob': 'whatsjob.p.rapidapi.com'
        }

        host = api_hosts.get(form.source.data, current_app.config.get('RAPIDAPI_HOST'))

        jobs_data = scrape_jobs_from_api(
            api_key, host, form.source.data,
            form.query.data, form.location.data, form.country.data
        )

        if jobs_data:
            # Handle different response formats
            if 'data' in jobs_data:
                job_list = jobs_data['data']
            elif isinstance(jobs_data, list):
                job_list = jobs_data
            else:
                job_list = []

            jobs_added = 0
            for job_data in job_list:
                # Check if job URL already exists
                existing_job = Job.query.filter_by(url=job_data.get('job_url', '')).first()
                if existing_job:
                    continue

                # Handle different API response formats
                if form.source.data in ['linkedin', 'indeed']:
                    title = job_data.get('title', '')
                    company = job_data.get('company', '')
                    location = job_data.get('location', '')
                    description = job_data.get('description', '')
                    url = job_data.get('url', '')
                    date_posted = None
                elif form.source.data == 'gupy':
                    title = job_data.get('title', '')
                    company = job_data.get('company', '')
                    location = job_data.get('location', '')
                    description = job_data.get('description', '')
                    url = job_data.get('url', '')
                    date_posted = None
                elif form.source.data == 'jobvacancies':
                    title = job_data.get('title', '')
                    company = job_data.get('company', '')
                    location = job_data.get('location', '')
                    description = job_data.get('description', '')
                    url = job_data.get('url', '')
                    date_posted = None
                elif form.source.data == 'whatsjob':
                    title = job_data.get('title', '')
                    company = job_data.get('company', '')
                    location = job_data.get('location', '')
                    description = job_data.get('description', '')
                    url = job_data.get('url', '')
                    date_posted = None
                else:
                    # Default JSearch format
                    title = job_data.get('job_title', '')
                    company = job_data.get('employer_name', '')
                    location = job_data.get('job_city', '') + ', ' + job_data.get('job_state', '')
                    description = job_data.get('job_description', '')
                    url = job_data.get('job_url', '')
                    date_posted = datetime.fromisoformat(job_data.get('job_posted_at_datetime_utc', '').replace('Z', '+00:00')) if job_data.get('job_posted_at_datetime_utc') else None

                job = Job(
                    title=title,
                    company=company,
                    location=location,
                    description=description,
                    url=url,
                    date_posted=date_posted,
                    source=form.source.data
                )
                db.session.add(job)
                jobs_added += 1

            db.session.commit()
            flash(f'Successfully added {jobs_added} new jobs!', 'success')
        else:
            flash('Failed to fetch jobs from API', 'danger')

        return redirect(url_for('main.index'))

    return render_template('scraper/scrape.html', title='Scrape Jobs', form=form)
