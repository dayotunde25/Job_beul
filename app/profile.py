from flask import render_template, redirect, url_for, flash, send_file
from flask_login import login_required, current_user
from __init__ import db
from app.profile import bp
from app.forms import ProfileForm
from app.utils import generate_cv_html, generate_cv_pdf
import os
import tempfile

@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.phone = form.phone.data
        current_user.address = form.address.data
        current_user.education = form.education.data
        current_user.experience = form.experience.data
        current_user.skills = form.skills.data
        current_user.summary = form.summary.data
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('profile.profile'))

    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.phone.data = current_user.phone
        form.address.data = current_user.address
        form.education.data = current_user.education
        form.experience.data = current_user.experience
        form.skills.data = current_user.skills
        form.summary.data = current_user.summary

    return render_template('profile/profile.html', title='Profile', form=form)

@bp.route('/cv/html')
@login_required
def generate_cv_html():
    cv_html = generate_cv_html(current_user)
    return render_template('profile/cv_preview.html', cv_html=cv_html, title='CV Preview')

@bp.route('/cv/pdf')
@login_required
def generate_cv_pdf():
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        filename = tmp_file.name

    try:
        generate_cv_pdf(current_user, filename)
        return send_file(filename, as_attachment=True, download_name='cv.pdf')
    finally:
        os.unlink(filename)
