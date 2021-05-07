from os import environ, path
from dotenv import load_dotenv
from flask import Config


class Config(object):
    """set flask configuration vars from .env file"""
    """basedir = path(.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir,'.env'))"""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
    TWITTER_OAUTH_CLIENT_KEY = environ.get("TWITTER_OAUTH_CLIENT_KEY")
    TWITTER_OAUTH_CLIENT_SECRET = environ.get("TWITTER_OAUTH_CLIENT_SECRET")
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'None'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = environ.get("MAIL_PASSWORD")

    class ProductionConfig(Config):
        DEBUG = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    class DevelopmentConfig(Config):
        ENV = "development"
        DEVELOPMENT = True
        SECRET_KEY = "secret_for_test_environment"
        OAUTHLIB_INSECURE_TRANSPORT = True
