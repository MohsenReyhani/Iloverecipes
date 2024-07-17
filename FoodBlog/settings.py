import os
from pathlib import Path
import django_heroku
import dj_database_url
from decouple import config
import boto3
import dj_database_url
import psycopg2


print("\n\n\n\YOU ARE USING SETTINGS.PY \n\n\n\n")
import json

from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DB_PASSWORD= os.environ.get('DB_PASSWORD')
NAME= os.environ.get('NAME')
DB_USER= os.environ.get('DB_USER')
SECRET_KEY=os.environ.get('SECRET_KEY')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY =os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME =os.environ.get('S3_BUCKET')


CLOUDFRONT_URL = 'https://d17usxoyp786nd.cloudfront.net/'  #TOOK OUT A / 11/6/23

DJANGO_STATIC = True

DJANGO_STATIC_FILE_PROXY = 'cloudfront.file_proxy'

COMPRESS_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
COMPRESS_ENABLED= True
COMPRESS_URL= CLOUDFRONT_URL

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Use S3 for media files storage

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#https://iloverecipes.s3.us-east-2.amazonaws.com/book_covers/Image.png





#MEDIA_URL = 'arn:aws:cloudfront::522349786223:distribution/ESJ9TIEAIRTU'



#S3_URL == #'https://iloverecipes.s3.us-east-2.amazonaws.com/'

MEDIA_URL = CLOUDFRONT_URL



CLOUDFRONT_PUB_KEY=os.getenv('CLOUDFRONT_PUB')

CLOUDFRONT_SECRET=os.getenv('CLOUDFRONT_SECRET')


AWS_DEFAULT_ACL='public-read'

AWS_S3_CUSTOM_DOMAIN = CLOUDFRONT_URL

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'recipes', 'static','recipes')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'recipes')




bucketurl='https://iloverecipes.s3.us-east-2.amazonaws.com'
DEBUG = True





ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'recipes',
    'compressor',
  #  'recipes.apps.RecipesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FoodBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'recipes', 'templates', 'recipes')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]


WSGI_APPLICATION = 'FoodBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        } 
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


MEDIA_URL_FROM_HOME= '../media/'


MEDIA_ROOT = os.path.join(BASE_DIR,'recipes','media')
print(MEDIA_ROOT)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_heroku.settings(locals())


DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER=os.environ.get('email')
EMAIL_HOST_PASSWORD=os.environ.get('mailpass')
EMAIL_USE_TLS= True
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'