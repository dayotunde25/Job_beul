from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, URL, Optional

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class ProfileForm(FlaskForm):
    # Basic Information
    first_name = StringField('First Name', validators=[Optional(), Length(max=64)])
    last_name = StringField('Last Name', validators=[Optional(), Length(max=64)])
    phone = StringField('Phone', validators=[Optional(), Length(max=20)])
    address = TextAreaField('Address', validators=[Optional()])
    city = StringField('City', validators=[Optional(), Length(max=100)])
    country = SelectField('Country', choices=[
        ('', 'Select Country'),
        ('us', 'United States'),
        ('ng', 'Nigeria'),
        ('ca', 'Canada'),
        ('fr', 'France'),
        ('uk', 'United Kingdom'),
        ('de', 'Germany'),
        ('au', 'Australia'),
        ('in', 'India'),
        ('br', 'Brazil')
    ], validators=[Optional()])
    linkedin_url = StringField('LinkedIn URL', validators=[Optional(), Length(max=200)])
    portfolio_url = StringField('Portfolio/Website URL', validators=[Optional(), Length(max=200)])

    # Professional Information
    current_position = StringField('Current Position', validators=[Optional(), Length(max=100)])
    years_of_experience = SelectField('Years of Experience', choices=[
        ('', 'Select Experience'),
        ('0', '0-1 years'),
        ('2', '2-3 years'),
        ('4', '4-5 years'),
        ('6', '6-10 years'),
        ('11', '11+ years')
    ], validators=[Optional()])
    education = TextAreaField('Education', validators=[Optional()])
    experience = TextAreaField('Work Experience', validators=[Optional()])
    skills = TextAreaField('Skills (comma-separated)', validators=[Optional()])
    certifications = TextAreaField('Certifications', validators=[Optional()])
    languages = TextAreaField('Languages', validators=[Optional()])
    summary = TextAreaField('Professional Summary', validators=[Optional()])

    # Job Preferences
    remote_work_preference = SelectField('Remote Work Preference', choices=[
        ('', 'No Preference'),
        ('remote', 'Remote Only'),
        ('hybrid', 'Hybrid'),
        ('onsite', 'On-site Only'),
        ('any', 'Any')
    ], validators=[Optional()])

    submit = SubmitField('Update Profile')

class JobSearchForm(FlaskForm):
    query = StringField('Job Title or Keywords', validators=[Optional()])
    location = StringField('Location', validators=[Optional()])
    company = StringField('Company', validators=[Optional()])
    submit = SubmitField('Search')

class ScraperForm(FlaskForm):
    source = SelectField('Job Source', choices=[
        ('all', 'Run All Sources'),
        ('whatjobs', 'WhatJobs API (Recommended)'),
        ('jsearch', 'JSearch API'),
        ('linkedin', 'LinkedIn Jobs (Web Scraping)'),
        ('indeed', 'Indeed Jobs (Web Scraping)'),
        ('glassdoor', 'Glassdoor Jobs (Web Scraping)'),
        ('remote_ok', 'RemoteOK (Remote Jobs)'),
        ('github_jobs', 'Tech Jobs (Curated)')
    ], validators=[DataRequired()])
    query = StringField('Search Query', validators=[Optional()])
    location = StringField('Location', validators=[Optional()])
    country = SelectField('Country', choices=[
        ('us', 'United States'),
        ('ng', 'Nigeria'),
        ('ca', 'Canada'),
        ('fr', 'France'),
        ('uk', 'United Kingdom'),
        ('de', 'Germany'),
        ('au', 'Australia'),
        ('in', 'India'),
        ('br', 'Brazil'),
        ('jp', 'Japan'),
        ('cn', 'China'),
        ('mx', 'Mexico'),
        ('ar', 'Argentina'),
        ('cl', 'Chile'),
        ('co', 'Colombia'),
        ('pe', 'Peru'),
        ('ve', 'Venezuela'),
        ('ec', 'Ecuador'),
        ('bo', 'Bolivia'),
        ('py', 'Paraguay'),
        ('uy', 'Uruguay')
    ], default='us', validators=[Optional()])
    submit = SubmitField('Start Scraping')
