from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from __init__ import db
from app.main import bp
from app.forms import JobSearchForm
from app.models import Job
from app.utils import get_job_recommendations
from sqlalchemy import or_, and_

@bp.route('/')
@bp.route('/index')
def index():
    page = request.args.get('page', 1, type=int)
    query = request.args.get('query', '')
    location = request.args.get('location', '')
    company = request.args.get('company', '')

    jobs_query = Job.query

    if query:
        jobs_query = jobs_query.filter(
            or_(Job.title.contains(query), Job.description.contains(query))
        )
    if location:
        jobs_query = jobs_query.filter(Job.location.contains(location))
    if company:
        jobs_query = jobs_query.filter(Job.company.contains(company))

    jobs = jobs_query.order_by(Job.created_at.desc()).paginate(
        page=page, per_page=10, error_out=False
    )

    next_url = url_for('main.index', page=jobs.next_num, query=query,
                      location=location, company=company) if jobs.has_next else None
    prev_url = url_for('main.index', page=jobs.prev_num, query=query,
                      location=location, company=company) if jobs.has_prev else None

    # Calculate starting ID for sequential numbering
    start_id = (page - 1) * 10 + 1

    form = JobSearchForm()
    if form.validate_on_submit():
        return redirect(url_for('main.index', query=form.query.data,
                               location=form.location.data, company=form.company.data))

    return render_template('main/index.html', title='Home',
                           jobs=jobs, form=form, query=query,
                           location=location, company=company, start_id=start_id)

@bp.route('/job/<int:id>')
def job_detail(id):
    job = Job.query.get_or_404(id)
    return render_template('main/job_detail.html', title=job.title, job=job)

@bp.route('/recommendations')
@login_required
def recommendations():
    if not current_user.is_authenticated:
        flash('Please log in to see job recommendations.', 'info')
        return redirect(url_for('auth.login'))

    recommended_jobs = get_job_recommendations(current_user, limit=20)

    if not recommended_jobs:
        flash('Complete your profile to get better job recommendations!', 'info')

    return render_template('main/recommendations.html', title='Job Recommendations',
                         jobs=recommended_jobs, user=current_user)
