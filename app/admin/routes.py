from flask import render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from functools import wraps
from __init__ import db
from app.admin import bp
from app.models import User, Job
from app.forms import ScraperForm
from app.utils import scrape_jobs_from_api
from app.enhanced_scraper import run_comprehensive_scraping
from sqlalchemy import func
from datetime import datetime, timedelta

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Admin access required.', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    # Get statistics
    total_jobs = Job.query.count()
    total_users = User.query.count()
    admin_users = User.query.filter_by(is_admin=True).count()

    # Jobs by source
    jobs_by_source = db.session.query(Job.source, func.count(Job.id)).group_by(Job.source).all()

    # Recent jobs (last 7 days)
    week_ago = datetime.utcnow() - timedelta(days=7)
    recent_jobs = Job.query.filter(Job.created_at >= week_ago).count()

    # Recent users (last 7 days)
    recent_users = User.query.filter(User.created_at >= week_ago).count()

    return render_template('admin/dashboard.html', title='Admin Dashboard',
                         total_jobs=total_jobs, total_users=total_users,
                         admin_users=admin_users, jobs_by_source=jobs_by_source,
                         recent_jobs=recent_jobs, recent_users=recent_users)

@bp.route('/users')
@login_required
@admin_required
def users():
    page = request.args.get('page', 1, type=int)
    users = User.query.order_by(User.created_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    return render_template('admin/users.html', title='User Management', users=users)

@bp.route('/users/<int:id>/toggle_admin', methods=['POST'])
@login_required
@admin_required
def toggle_admin(id):
    user = User.query.get_or_404(id)
    if user == current_user:
        flash('You cannot modify your own admin status.', 'danger')
    else:
        user.is_admin = not user.is_admin
        db.session.commit()
        flash(f'Admin status for {user.username} has been {"granted" if user.is_admin else "revoked"}.', 'success')
    return redirect(url_for('admin.users'))

@bp.route('/jobs')
@login_required
@admin_required
def jobs():
    page = request.args.get('page', 1, type=int)
    source = request.args.get('source', '')
    query_filter = request.args.get('query', '')

    jobs_query = Job.query

    if source:
        jobs_query = jobs_query.filter_by(source=source)

    if query_filter:
        jobs_query = jobs_query.filter(
            db.or_(
                Job.title.contains(query_filter),
                Job.company.contains(query_filter),
                Job.description.contains(query_filter)
            )
        )

    jobs = jobs_query.order_by(Job.created_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )

    # Get unique sources for filter dropdown
    sources = db.session.query(Job.source).distinct().all()
    sources = [s[0] for s in sources]

    # Calculate starting ID for sequential numbering
    start_id = (page - 1) * 20 + 1

    return render_template('admin/jobs.html', title='Job Management',
                         jobs=jobs, sources=sources, current_source=source,
                         current_query=query_filter, start_id=start_id)

@bp.route('/jobs/<int:id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_job(id):
    job = Job.query.get_or_404(id)
    db.session.delete(job)
    db.session.commit()
    flash('Job has been deleted.', 'success')
    return redirect(url_for('admin.jobs'))

@bp.route('/scraper', methods=['GET', 'POST'])
@login_required
@admin_required
def scraper():
    form = ScraperForm()
    if form.validate_on_submit():
        api_key = current_app.config.get('RAPIDAPI_KEY')
        if not api_key:
            flash('RapidAPI key not configured', 'danger')
            return redirect(url_for('admin.scraper'))

        # Determine scraping sources
        scraping_sources = {
            'whatjobs': 'api.whatjobs.com',
            'jsearch': 'jsearch.p.rapidapi.com',
            'linkedin': 'linkedin.com',
            'indeed': 'indeed.com',
            'glassdoor': 'glassdoor.com',
            'remote_ok': 'remoteok.io',
            'github_jobs': 'github.com'
        }

        # If admin wants to run all sources
        if form.source.data == 'all':
            sources_to_run = list(scraping_sources.keys())
        else:
            sources_to_run = [form.source.data]

        total_jobs_added = 0
        total_jobs_scraped = 0

        # Countries to scrape from
        countries = ['us', 'ng', 'ca', 'fr']

        flash(f'Starting scraping from sources: {", ".join(sources_to_run)}', 'info')

        for source in sources_to_run:
            host = scraping_sources.get(source, current_app.config.get('RAPIDAPI_HOST', 'jsearch.p.rapidapi.com'))

            for country in countries:
                # Scrape jobs for each country
                jobs_data = scrape_jobs_from_api(
                    api_key, host, source,
                    'software developer', None, country
                )

                if jobs_data:
                    jobs_added = 0

                    # Handle different response structures
                    if isinstance(jobs_data, list):
                        jobs_list = jobs_data
                    elif isinstance(jobs_data, dict):
                        jobs_list = jobs_data.get('data', []) if isinstance(jobs_data.get('data'), list) else [jobs_data]
                    else:
                        jobs_list = []

                    for job_data in jobs_list:
                        if not job_data or not isinstance(job_data, dict):
                            continue

                        # Use unified field extraction
                        title = (job_data.get('job_title') or job_data.get('title') or
                                job_data.get('position') or '')
                        company = (job_data.get('employer_name') or job_data.get('company') or
                                  job_data.get('companyName') or '')
                        location = (job_data.get('job_city', '') + ', ' + job_data.get('job_state', '') if
                                   job_data.get('job_city') else job_data.get('location') or
                                   job_data.get('jobGeo') or '')
                        description = (job_data.get('job_description') or job_data.get('description') or
                                      job_data.get('jobDescription') or 'No description available')
                        url = (job_data.get('job_url') or job_data.get('url') or
                              job_data.get('link') or '')

                        # Handle date parsing
                        date_posted = None
                        date_str = (job_data.get('job_posted_at_datetime_utc') or
                                   job_data.get('datePosted') or job_data.get('pubDate'))
                        if date_str:
                            try:
                                date_posted = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                            except:
                                date_posted = None

                        # Skip if essential fields are missing
                        if not title or not url:
                            continue

                        # Check if job URL already exists (prevent autoflush)
                        with db.session.no_autoflush:
                            existing_job = Job.query.filter_by(url=url).first()
                        if existing_job:
                            continue

                        job = Job(
                            title=title,
                            company=company,
                            location=location.strip(', '),
                            description=description[:1000],  # Limit description length
                            url=url,
                            date_posted=date_posted,
                            source=source
                        )
                        db.session.add(job)
                        jobs_added += 1

                    # Commit after processing each country's jobs to prevent database locks
                    if jobs_added > 0:
                        db.session.commit()

                    total_jobs_added += jobs_added

        db.session.commit()
        if total_jobs_added > 0:
            flash(f'Successfully added {total_jobs_added} new jobs from {len(sources_to_run)} source(s)!', 'success')
        else:
            flash('No new jobs were found or added.', 'info')

        return redirect(url_for('admin.dashboard'))

    return render_template('admin/scraper.html', title='Admin Scraper', form=form)

@bp.route('/comprehensive-scraper', methods=['GET', 'POST'])
@login_required
@admin_required
def comprehensive_scraper():
    """Run comprehensive job scraping using BeautifulSoup approach"""
    if request.method == 'POST':
        try:
            flash('Starting comprehensive job scraping with real-time database insertion... This may take several minutes.', 'info')

            # Run the comprehensive scraping (jobs are saved automatically during scraping)
            all_jobs = run_comprehensive_scraping()

            # The jobs are already saved to the database during scraping
            total_jobs_found = len(all_jobs)

            if total_jobs_found > 0:
                flash(f'Comprehensive scraping completed! Found {total_jobs_found} jobs total. Jobs were saved to database in real-time during scraping.', 'success')
            else:
                flash('Comprehensive scraping completed but no new jobs were found.', 'info')

        except Exception as e:
            flash(f'Error during comprehensive scraping: {str(e)}', 'danger')
            print(f"Comprehensive scraping error: {e}")

    return render_template('admin/comprehensive_scraper.html', title='Comprehensive Job Scraper')
