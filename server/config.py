import os
from pathlib import Path


class Config:
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    SECRET_KEY = os.getenv('SECRET_KEY', 'strong-secret-key')
    BASE_DIR = Path(__file__).resolve().parent.parent
    SQLALCHEMY_ECHO = True


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DATABASE_URL = 'sqlite:///:memory:'
    # DATABASE_URL = 'sqlite:///test.db.sqlite3'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
