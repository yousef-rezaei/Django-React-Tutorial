import os
from urllib.parse import urlparse, parse_qs
# from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['WEBSITE_HOSTNAME']]
DEBUG = False
SECRET_KEY = os.environ['MY_SECRET_KEY']


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'Whitenoise.middleware.WhiteNoiseMiddleware',
    # Ensure Whitenoise is before SessionMiddleware
    # to serve static files correctly
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS_ALLOWED_ORIGINS = [
# ]


STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
        
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
      
    }
}


# CONNECTION = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
# CONNECTION_STR = {pair.split('=')[0]: pair.split('=')[1] for pair in CONNECTION.split(' ')}
# # Database


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": CONNECTION_STR["dbname"],
#         "HOST": CONNECTION_STR["host"],
#         "USER": CONNECTION_STR["user"],
#         "PASSWORD": CONNECTION_STR["password"],
       
#     }
# }

url = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
parsed = urlparse(url)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": parsed.path[1:],  # remove leading slash
        "USER": parsed.username,
        "PASSWORD": parsed.password,
        "HOST": parsed.hostname,
        "PORT": parsed.port,
        "OPTIONS": {
            "sslmode": parse_qs(parsed.query).get("sslmode", ["require"])[0]
        }
    }
}

# we dont need beacuse we get it from settings.py
# STATIC_ROOT = BASE_DIR / 'staticfiles'
