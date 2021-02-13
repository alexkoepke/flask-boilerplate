import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'customer-hub.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail Configs
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # if os.environ.get('ADMIN_EMAIL') is not None:
    #     ADMINS = os.environ.get('ADMIN_EMAIL').split(",")
    # else:
    #     ADMINS = os.environ.get('ADMIN_EMAIL')
    LANGUAGES = ['en', 'es']
    # POSTS_PER_PAGE = 3
    # TRANSLATOR_TEXT_SUBSCRIPTION_KEY = os.environ.get('TRANSLATOR_TEXT_SUBSCRIPTION_KEY')
    # TRANSLATOR_TEXT_ENDPOINT = os.environ.get('TRANSLATOR_TEXT_ENDPOINT')
    # TRANSLATOR_TEXT_REGION = os.environ.get('TRANSLATOR_TEXT_REGION')

    ## SEARCH
    # ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    # ELASTICSEARCH_PASSWORD = os.environ.get('ELASTICSEARCH_PASSWORD')
