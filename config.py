from dotenv import load_dotenv
load_dotenv()

import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-12345'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///college_app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
