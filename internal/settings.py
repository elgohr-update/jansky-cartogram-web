import os

CARTOGRAM_EXE = os.environ['CARTOGRAM_EXE']
CARTOGRAM_DATA_DIR = os.environ['CARTOGRAM_DATA_DIR']
CARTOGRAM_COLOR = os.environ['CARTOGRAM_COLOR']
DEBUG = True if os.environ['CARTOGRAM_DEBUG'].lower() == "true" else False
DATABASE_URI = os.environ['CARTOGRAM_DATABASE_URI']
USE_DATABASE = True if os.environ['CARTOGRAM_USE_DATABASE'].lower() == "true" else False

HOST = os.environ['CARTOGRAM_HOST']
PORT = int(os.environ['CARTOGRAM_PORT'])

VERSION = os.environ['CARTOGRAM_VERSION']

SMTP_HOST = os.environ['CARTOGRAM_SMTP_HOST']
SMTP_PORT = int(os.environ['CARTOGRAM_SMTP_PORT'])
SMTP_AUTHENTICATION_REQUIRED = True if os.environ['CARTOGRAM_SMTP_AUTHENTICATION_REQUIRED'].lower() == "true" else False
SMTP_USER = os.environ['CARTOGRAM_SMTP_USER']
SMTP_PASSWORD = os.environ['CARTOGRAM_SMTP_PASSWORD']
SMTP_FROM_EMAIL = os.environ['CARTOGRAM_SMTP_FROM_EMAIL']
SMTP_DESTINATION = os.environ['CARTOGRAM_SMTP_DESTINATION']

CARTOGRAM_LAMBDA_URL = os.environ['CARTOGRAM_LAMBDA_URL']
CARTOGRAM_LAMDA_API_KEY = os.environ['CARTOGRAM_LAMBDA_API_KEY']

CARTOGRAM_PROGRESS_SECRET = os.environ['CARTOGRAM_PROGRESS_SECRET']
CARTOGRAM_REDIS_HOST = os.environ['CARTOGRAM_REDIS_HOST']
CARTOGRAM_REDIS_PORT = int(os.environ['CARTOGRAM_REDIS_PORT'])