import os

from dotenv import load_dotenv


load_dotenv()

DJANGO_SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
DJANGO_PORT = os.environ.get('DJANGO_PORT')
DJANGO_HOST = os.environ.get('DJANGO_HOST')
GOOGLE_OAUTH2_KEY = os.environ.get('GOOGLE_OAUTH2_KEY')
GOOGLE_OAUTH2_SECRET = os.environ.get('GOOGLE_OAUTH2_SECRET')