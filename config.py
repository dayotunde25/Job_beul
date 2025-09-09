<<<<<<< HEAD
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///jobs.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RAPIDAPI_KEY = os.environ.get('RAPIDAPI_KEY')
    WTF_CSRF_ENABLED = True
    LOG_LEVEL = 'INFO'
=======
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///jobs.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RAPIDAPI_KEY = os.environ.get('RAPIDAPI_KEY')
    WTF_CSRF_ENABLED = True
    LOG_LEVEL = 'INFO'
>>>>>>> 24806e06812e7a8caf53d6dd5ce6b2ee56a9d86f
