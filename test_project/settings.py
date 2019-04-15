"""
Django settings for empty project.

Generated by 'django-admin startproject' using Django 1.11.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)
BASE_DIR_NAME = os.path.basename(BASE_DIR)
SERVICE_NAME = os.environ.get('SERVICE_NAME', BASE_DIR_NAME)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+!1n5nglwv!@i^od9f9+srz$0*u_*(k0k)ann3@3uc$f#1*b6i'  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tests_storage',
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

ROOT_URLCONF = 'test_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASE_URL = os.environ.get(
    'DATABASE_URL',
    'postgres://postgres:postgres@127.0.0.1:5432/' + SERVICE_NAME)

DATABASES = {
    'default': dj_database_url.parse(
        DATABASE_URL,
        engine='django.contrib.gis.db.backends.postgis',
        conn_max_age=60 * 5)
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MINIO_STORAGE_ENDPOINT = os.environ.get('MINIO_STORAGE_ENDPOINT',
                                        'localhost:9000')
MINIO_STORAGE_ACCESS_KEY = os.environ.get('MINIO_STORAGE_ACCESS_KEY', '')
MINIO_STORAGE_SECRET_KEY = os.environ.get('MINIO_STORAGE_SECRET_KEY', '')
MINIO_STORAGE_BUCKET_NAME = os.environ.get('MINIO_STORAGE_BUCKET_NAME',
                                           'test-bucket')

# humanfriendly value
# see: https://humanfriendly.readthedocs.io/en/latest/readme.html#a-note-about-size-units  # noqa
MINIO_STORAGE_MAX_FILE_SIZE = '100B'
# Необходимо промигрировать базу при изменении этого значения
MINIO_STORAGE_MAX_FILE_NAME_LEN = 100
MINIO_STORAGE_MAX_FILES_COUNT = 2

try:
    from .settings_local import *  # noqa: pylint=unused-wildcard-import, pylint=wildcard-import
except ImportError:
    pass