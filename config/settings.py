from config import local_config

SQLALCHEMY_DATABASE_URL = local_config.SQLALCHEMY_DATABASE_URL

SECRET_KEY = local_config.SECRET_KEY
API_V1_STR = "/api/v1"

PROJECT_NAME = "COVOLUNTARY"
SERVER_HOST = "http://tymkiv.pp.ua/"

ACCESS_TOKEN_EXPIRE_MINUTES = 30
EMAIL_RESET_TOKEN_EXPIRE_HOURS = 5

USERS_OPEN_REGISTRATION = True
EMAILS_ENABLED = True

EMAILS_FROM_NAME = local_config.EMAILS_FROM_NAME
EMAILS_FROM_EMAIL = local_config.EMAILS_FROM_EMAIL
EMAIL_TEMPLATES_DIR = "app/email-templates/build"

SMTP_HOST = local_config.SMTP_HOST
SMTP_PORT = local_config.SMTP_PORT
SMTP_TLS = local_config.SMTP_TLS
SMTP_USER = local_config.SMTP_USER
SMTP_PASSWORD = local_config.SMTP_PASSWORD
