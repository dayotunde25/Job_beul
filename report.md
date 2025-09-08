# CHAPTER FOUR

## 4.0 Implementation

This chapter describes the implementation of the job board system. It covers the software and hardware requirements, the system implementation details, the graphical user interface, and a discussion of the results.

## 4.1 Software Requirement

The system is developed using the Python programming language and the Flask web framework. The following are the key software requirements:

*   **Programming Language:** Python 3.x
*   **Web Framework:** Flask 2.3.3
*   **Database:** Flask-SQLAlchemy 3.0.5 (which uses SQLAlchemy, a SQL toolkit that can work with various databases like SQLite, PostgreSQL, MySQL, etc. In this project, it is using SQLite as evidenced by the `instance/jobs.db` file).
*   **Authentication:** Flask-Login 0.6.3
*   **Forms:** Flask-WTF 1.1.1, WTForms 3.0.1
*   **Email Validation:** email-validator 2.1.0
*   **HTTP Requests:** requests 2.31.0 (for the scraper to fetch data from RapidAPI)
*   **Environment Variables:** python-dotenv 1.0.0
*   **PDF Generation:** reportlab 4.0.4 (for CV generation)
*   **Scheduled Tasks:** APScheduler 3.10.4 (for periodic scraping)
*   **Frontend Framework:** Flask-Bootstrap 3.3.7.1, Bootstrap 5, Animate.css, Font Awesome
*   **Image Processing:** Pillow 10.0.1
*   **WSGI Utility:** Werkzeug 2.3.7
*   **API Integration**: RapidAPI for job scraping

## 4.2 Hardware Requirement

The following are the minimum hardware requirements for running the system:

*   **Processor:** 1 GHz or faster processor
*   **RAM:** 512 MB of RAM
*   **Hard Disk:** 1 GB of free hard disk space
*   **Operating System:** Windows, macOS, or Linux

## 4.3 System Implementation

The system is implemented as a modular Flask web application. The application is structured using Flask Blueprints to separate concerns and organize the codebase. The main components of the system are:

*   **`app` directory:** This is the main application package.
    *   **`__init__.py`:** The Flask application factory. Initializes the Flask application, extensions, and database.
*   **`auth` blueprint:** Handles user authentication. This includes user registration with a username, email, and password; a login page with a "remember me" option; and a logout function. The system securely handles passwords by hashing them and provides feedback to the user through flashed messages.
*   **`main` blueprint:** Contains the core application logic, such as displaying the main pages with job listings, job details, and search functionality. The search functionality allows users to search for jobs by query (title or description), location, and company. The results are paginated, displaying 10 jobs per page.
*   **`profile` blueprint:** Manages user profiles and CV generation. Users can update their personal information, education, work experience, skills, and a summary. The application can then generate a preview of the CV in HTML format and allow the user to download a PDF version.
*   **`scraper` blueprint:** Contains the logic for scraping job data from external sources via RapidAPI. The scraper can fetch jobs from multiple sources, including JSearch, LinkedIn, Indeed, Greenhouse, Jooble, Gupy, Job Vacancies, and WhatsJob. It handles different API response formats and avoids adding duplicate jobs by checking the job URL.
*   **`admin` blueprint:** Provides a comprehensive administrative interface. This includes a dashboard with site statistics (total jobs, users, etc.), user management (viewing users and toggling admin status), job management (viewing, filtering, and deleting jobs), and a scraper management page to manually trigger the job scraping process for specific or all available sources. Access to this blueprint is restricted to users with admin privileges.
    *   **`models.py`:** Defines the database models (User, Job, etc.) using Flask-SQLAlchemy.
    *   **`forms.py`:** Defines the application's forms using Flask-WTF.
    *   **`utils.py`:** Contains utility functions, including the CV generation logic.
*   **`run.py`:** The main entry point for running the application.
*   **`config.py`:** Contains the application's configuration settings.
*   **`create_admin.py`:** A script for creating an administrative user.
*   **`instance/jobs.db`:** The SQLite database file.
*   **`templates` directory:** Contains the Jinja2 HTML templates for the application, organized by blueprint.
*   **`static` directory:** Contains static assets such as CSS, JavaScript, and images.

## 4.4 Display of Graphical User Interface

The graphical user interface (GUI) is built using HTML, CSS, and the Bootstrap framework. The templates are rendered by Flask using the Jinja2 templating engine.

**[SCREENSHOT REQUIRED]** - A screenshot of the **Home Page** (`app/templates/main/index.html`) should be included here to show the main landing page of the job board.

**[SCREENSHOT REQUIRED]** - A screenshot of the **Registration Page** (`app/templates/auth/register.html`) should be included here to show the user registration form.

**[SCREENSHOT REQUIRED]** - A screenshot of the **Login Page** (`app/templates/auth/login.html`) should be included here to show the user login form.

**[SCREENSHOT REQUIRED]** - A screenshot of the **User Profile Page** (`app/templates/profile/profile.html`) should be included here to show where users can manage their profile information.

**[SCREENSHOT REQUIRED]** - A screenshot of the **Job Detail Page** (`app/templates/main/job_detail.html`) should be included here to show how a single job posting is displayed.

**[SCREENSHOT REQUIRED]** - A screenshot of the **Admin Dashboard** (`app/templates/admin/dashboard.html`) should be included here to show the main administrative interface.

## 4.5 Results and Discussion

The implementation of the job board system was successful. The system meets all the functional requirements, including user authentication, job scraping from RapidAPI, advanced job searching and filtering, user profile management, and automatic CV generation in both HTML and PDF formats. The use of the Flask framework and its extensions allowed for rapid development and a modular, maintainable codebase. The Bootstrap framework, along with Animate.css and Font Awesome, provides a responsive and modern user-friendly interface. The scraper effectively collects job data, and the admin panel provides the necessary tools for managing the system. The application also includes important security features such as password hashing, CSRF protection, and secure session management.

# CHAPTER FIVE

## 5.0 Conclusion and Recommendations

This chapter provides a conclusion to the project and offers recommendations for future work.

## 5.1 Conclusion

This project successfully designed and implemented a web-based job board system. The system provides a platform for job seekers to find and apply for jobs, and for administrators to manage the system. The project demonstrated the use of modern web development technologies, including Python, Flask, and SQLAlchemy. The final system is a functional and user-friendly application that can be extended with additional features in the future.

## 5.2 Recommendations

The following are some recommendations for future work on the project:

*   **Employer Accounts:** Add functionality for employers to create accounts, post job listings directly, and manage applications.
*   **Email Notifications:** Implement email notifications to inform users about new job postings that match their profile and the status of their applications.
*   **Database Migration to PostgreSQL:** For a production environment, migrating from SQLite to a more robust database like PostgreSQL is recommended.
*   **Dockerization:** The `README.md` provides a `Dockerfile`, which is a great starting point. This can be further improved for a production-ready deployment.
*   **API for Mobile App:** Develop a RESTful API to allow for the creation of a mobile application for the job board.
*   **Deployment to a Live Server:** Deploy the application to a cloud platform like Heroku, AWS, or Azure to make it publicly accessible.
*   **Improved Scraping:** Enhance the scraper to handle more complex websites, including those that require JavaScript to render content, and to scrape from a wider variety of sources.
