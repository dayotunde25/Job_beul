import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('RAPIDAPI_KEY')

ENDPOINTS = {
    'active_jobs': {
        'url': 'https://active-jobs-db.p.rapidapi.com/active-jb-7d',
        'host': 'active-jobs-db.p.rapidapi.com'
    },
    'jsearch': {
        'url': 'https://jsearch.p.rapidapi.com/search',
        'host': 'jsearch.p.rapidapi.com'
    },
    'internships': {
        'url': 'https://internships-api.p.rapidapi.com/active-jb-7d',
        'host': 'internships-api.p.rapidapi.com'
    }
}

HEADERS_TEMPLATE = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': ''
}

DATA_DIR = 'data'
LOG_FILE = 'scraper.log'
