from flask import render_template, redirect, url_for, flash, request, send_file
from flask_login import login_required, current_user
from __init__ import db
from app.profile import bp
from app.forms import ProfileForm
from app.utils import generate_cv_html, generate_cv_pdf
import os

@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        # Basic Information
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.phone = form.phone.data
        current_user.address = form.address.data
        current_user.city = form.city.data
        current_user.country = form.country.data
        current_user.linkedin_url = form.linkedin_url.data
        current_user.portfolio_url = form.portfolio_url.data

        # Professional Information
        current_user.current_position = form.current_position.data
        current_user.years_of_experience = int(form.years_of_experience.data) if form.years_of_experience.data else None
        current_user.education = form.education.data
        current_user.experience = form.experience.data
        current_user.skills = form.skills.data
        current_user.certifications = form.certifications.data
        current_user.languages = form.languages.data
        current_user.summary = form.summary.data
        current_user.remote_work_preference = form.remote_work_preference.data

        # Update profile completeness
        current_user.update_profile_completeness()

        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('profile.profile'))
    elif request.method == 'GET':
        # Basic Information
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.phone.data = current_user.phone
        form.address.data = current_user.address
        form.city.data = current_user.city
        form.country.data = current_user.country
        form.linkedin_url.data = current_user.linkedin_url
        form.portfolio_url.data = current_user.portfolio_url

        # Professional Information
        form.current_position.data = current_user.current_position
        form.years_of_experience.data = str(current_user.years_of_experience) if current_user.years_of_experience else ''
        form.education.data = current_user.education
        form.experience.data = current_user.experience
        form.skills.data = current_user.skills
        form.certifications.data = current_user.certifications
        form.languages.data = current_user.languages
        form.summary.data = current_user.summary
        form.remote_work_preference.data = current_user.remote_work_preference

    return render_template('profile/profile.html', title='Profile', form=form, user=current_user)

@bp.route('/cv/preview')
@login_required
def cv_preview():
    cv_html = generate_cv_html(current_user)
    return render_template('profile/cv_preview.html', title='CV Preview', cv_html=cv_html)

@bp.route('/cv/download')
@login_required
def cv_download():
    filename = f'cv_{current_user.username}.pdf'
    filepath = os.path.join('temp', filename)
    os.makedirs('temp', exist_ok=True)
    generate_cv_pdf(current_user, filepath)
    return send_file(filepath, as_attachment=True, download_name=filename)
