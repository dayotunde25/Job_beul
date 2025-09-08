# JobBoard - Flask Job Board Application

A modern, full-featured job board application built with Flask, featuring web scraping, user authentication, profile management, and CV generation.

## Features

- **Job Scraping**: Automated job data collection from multiple sources using RapidAPI
- **User Authentication**: Secure registration, login, and logout with Flask-Login
- **Profile Management**: Complete user profiles with personal and professional information
- **CV Generation**: Automatic HTML and PDF CV generation from user profiles
- **Job Search & Filtering**: Advanced search and filter capabilities
- **Responsive Design**: Beautiful Bootstrap UI with animations and modern styling
- **Admin Features**: Administrative controls for scraper management
- **Security**: Password hashing, CSRF protection, and session security

## Technology Stack

- **Backend**: Python 3.9+, Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF with WTForms
- **UI**: Bootstrap 5, Animate.css, Font Awesome
- **PDF Generation**: ReportLab
- **API Integration**: RapidAPI for job scraping

## Project Structure

```
JobBoard/
├── app/
│   ├── __init__.py          # Flask application factory
│   ├── models.py            # Database models (User, Job)
│   ├── auth/                # Authentication blueprint
│   │   ├── __init__.py
│   │   ├── routes.py        # Auth routes (login, register, logout)
│   │   └── forms.py         # Auth forms
│   ├── main/                # Main application blueprint
│   │   ├── __init__.py
│   │   ├── routes.py        # Main routes (home, search)
│   │   └── forms.py         # Search forms
│   ├── scraper/             # Scraper blueprint
│   │   ├── __init__.py
│   │   ├── routes.py        # Scraper management routes
│   │   └── scraper.py       # Job scraping logic
│   ├── profile/             # Profile blueprint
│   │   ├── __init__.py
│   │   ├── routes.py        # Profile management routes
│   │   ├── forms.py         # Profile forms
│   │   └── utils.py         # CV generation utilities
│   └── forms.py             # Shared forms
├── templates/               # Jinja2 templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   └── cv_template.html
├── static/                  # Static assets
│   ├── css/
│   ├── js/
│   └── images/
├── instance/                # Instance-specific data
├── config.py                # Configuration settings
├── run.py                   # Application entry point
├── create_admin.py          # Admin user creation script
├── requirements.txt         # Python dependencies
└── README.md
```

## Installation & Setup

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Git (optional)

### 1. Clone or Download the Project

```bash
git clone <repository-url>
cd JobBoard
```

### 2. Create Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
RAPIDAPI_KEY=your-rapidapi-key-here
RAPIDAPI_HOST=jsearch.p.rapidapi.com
DATABASE_URL=sqlite:///jobs.db
```

#### Getting RapidAPI Key

1. Go to [RapidAPI](https://rapidapi.com/)
2. Search for job search APIs (e.g., JSearch, LinkedIn Jobs, Indeed Jobs)
3. Subscribe to your preferred API
4. Copy your API key from the dashboard

### 5. Initialize Database

```bash
# Create admin user (optional)
python create_admin.py

# The database will be automatically created when you first run the app
```

### 6. Run the Application

```bash
python run.py
```

The application will be available at `http://127.0.0.1:5000`

## Usage

### User Registration & Login

1. Visit the home page
2. Click "Register" to create a new account
3. Fill in your details and submit
4. Login with your credentials

### Profile Management

1. After logging in, access your profile
2. Fill in personal and professional information
3. Save your profile

### CV Generation

1. Complete your profile information
2. Navigate to the CV section
3. Generate HTML or PDF versions of your CV
4. Download or view your CV

### Job Search

1. Use the search form on the home page
2. Enter keywords, location, or company
3. Browse and filter job results

### Admin Features

1. Login with admin credentials
2. Access scraper management
3. Trigger manual scraping
4. View scraping logs

## API Endpoints

### Authentication
- `GET/POST /auth/login` - User login
- `GET/POST /auth/register` - User registration
- `GET /auth/logout` - User logout

### Main Application
- `GET /` - Home page with job search
- `GET /index` - Job listings page

### Profile Management
- `GET/POST /profile` - View/edit profile
- `GET /profile/cv` - Generate CV

### Scraper (Admin Only)
- `GET /scraper` - Scraper dashboard
- `POST /scraper/trigger` - Manual scraper trigger

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Flask secret key | dev-secret-key |
| `RAPIDAPI_KEY` | RapidAPI key for job scraping | None |
| `RAPIDAPI_HOST` | RapidAPI host | jsearch.p.rapidapi.com |
| `DATABASE_URL` | Database connection string | sqlite:///jobs.db |
| `LOG_LEVEL` | Logging level | INFO |

### Database Configuration

The application uses SQLite by default. For production, consider using PostgreSQL:

```env
DATABASE_URL=postgresql://user:password@localhost/fepil_jobs
```

## Development

### Running in Debug Mode

```bash
export FLASK_ENV=development
python run.py
```

### Database Migrations

For schema changes, you may need to recreate the database:

```bash
# Stop the application
# Delete the database file
rm instance/jobs.db
# Restart the application (it will recreate tables)
```

### Adding New Features

1. Create new blueprints in the `app/` directory
2. Register blueprints in `app/__init__.py`
3. Add routes and templates as needed
4. Update forms and models if required

## Security Features

- **Password Hashing**: Uses Werkzeug's secure password hashing
- **CSRF Protection**: Enabled for all forms
- **Session Security**: Secure session management
- **Input Validation**: Server-side validation for all forms
- **SQL Injection Prevention**: Uses SQLAlchemy ORM

## Deployment

### Production Deployment

1. Set `FLASK_ENV=production` in environment
2. Use a production WSGI server (e.g., Gunicorn)
3. Configure a reverse proxy (e.g., Nginx)
4. Set strong `SECRET_KEY`
5. Use a production database (PostgreSQL recommended)

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "run.py"]
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue on GitHub
- Check the documentation
- Review the code comments

## Changelog

### Version 1.0.0
- Initial release
- Basic job board functionality
- User authentication
- Profile management
- CV generation
- Job scraping integration

---

**JobBoard** - Your gateway to amazing career opportunities! 🚀
