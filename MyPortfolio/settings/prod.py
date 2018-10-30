from .base import *
import django_heroku

# SECRET KEY
SECRET_KEY = os.environ["SECRET_KEY"]

# DEBUG
DEBUG = False

# BASE URL AND ALLOWED HOSTS
BASE_URL = "https://www.mark-petersen.dk"
ALLOWED_HOSTS = ['mark-petersen.herokuapp.com', '.mark-petersen.dk']

# EMAIL
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'xxxx'
EMAIL_HOST_USER = 'xxxx@gmail.com'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# SSL AND SECURITY
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# HEROKU
import django_heroku
django_heroku.settings(locals())