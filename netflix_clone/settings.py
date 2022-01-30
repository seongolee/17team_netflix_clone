"""
Django settings for netflix_clone project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import json
import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
import pymysql

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

secret_file = os.path.join(BASE_DIR, 'secrets.json')
with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'sign_up',
    'find_user',
    'logout',
    'main',
    'login',
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

ROOT_URLCONF = 'netflix_clone.urls'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# 임시 주석 이부분 살리면 static 경로가 안먹힘.
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

with open(os.path.join(BASE_DIR, 'aws.json')) as f:
    secrets = json.loads(f.read())

AWS_ACCESS_KEY_ID = secrets['AWS']['ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secrets['AWS']['SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secrets['AWS']['STORAGE_BUCKET_NAME']
AWS_DEFAULT_ACL = 'public-read'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()

WSGI_APPLICATION = 'netflix_clone.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': secrets['default']['ENGINE'],
        'NAME': secrets['default']['NAME'],
        'USER': secrets['default']['USER'],
        'PASSWORD': secrets['default']['PASSWORD'],
        'HOST': secrets['default']['HOST'],
        'PORT': secrets['default']['PORT']
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'user.UserModel'

LOGIN_URL = 'sign_up_check'

# 메일을 호스트하는 서버
EMAIL_HOST = secrets['MAIL']['EMAIL_HOST']
# gmail과의 통신하는 포트
EMAIL_PORT = secrets['MAIL']['EMAIL_PORT']
# 발신할 이메일
EMAIL_HOST_USER = secrets['MAIL']['EMAIL_HOST_USER']
# 발신할 메일의 비밀번호
EMAIL_HOST_PASSWORD = secrets['MAIL']['EMAIL_HOST_PASSWORD']
# TLS 보안 방법
EMAIL_USE_TLS = secrets['MAIL']['EMAIL_USE_TLS']

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

