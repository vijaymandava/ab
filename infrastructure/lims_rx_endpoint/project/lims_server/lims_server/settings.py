"""
Django settings for lims_server project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ep#(s^d&ic(1zuno628(303fxe8&y#ay17lfz87a)dcjc)85@&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'app_sm_rx.apps.AppSmRxConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    # 'app_sm_rx.',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lims_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'lims_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
        # 'level': 'WARNING',
    },
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


# '2021-12-12T12:00:14.858000'
# MY_DATETIME_FORMAT = 'iso-8601',
# MY_DATETIME_INPUT_FORMAT = ['YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]', 'foobar123']

#, 'status_update_time': '1/7/2021 12:08:22 PM'}


REST_FRAMEWORK = {

    # [("%m/%d/%Y %I:%M:ss %p"),],   does not work

    'DATETIME_FORMAT': 'iso-8601',
    'DATETIME_INPUT_FORMATS': [(r"%m/%d/%Y %I:%M:ss %p"), ],

    'DATE_FORMAT': 'iso-8601',
    'DATE_INPUT_FORMATS': [(r"%m/%d/%Y %I:%M:ss %p"), ],

    'TIME_FORMAT': 'iso-8601',
    'TIME_INPUT_FORMATS': [(r"%m/%d/%Y %I:%M:ss %p"), ],
}
    # 'DATETIME_FORMAT': '%m/%d/%Y %I:%M:ss %p',
    # # 'DATETIME_INPUT_FORMATS': [
    # #     'iso-8601',
    # #     'MM/DD/YYYY hh:mm:ss [.uuuuuu]][+HH:MM|-HH:MM|Z].',  
    # #     '%m/%d/%Y %I:%M:ss %p',  # '1/7/2021 12:08:22 PM'
    # # ],

    # 'DATETIME_INPUT_FORMATS': [
    #     '%m/%d/%Y %I:%M:ss %p',  # '1/7/2021 12:08:22 PM'
    # ],

    # #     'YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]',
    # #     'M/D/YYYY hh:mm:ss[.*]',
    # #     'foobar123',
    # #     # 'MM/DD/YYYY hh:mm:ss',  # '1/7/2021 12:08:22 PM'
    # #     'YYYY/MM/DD hh:mm:ss',  # '1/7/2021 12:08:22 PM'


    # # 'DATE_FORMAT': 'iso-8601',
    # # 'DATE_INPUT_FORMATS': ['YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]', 'foobar456'],

    # # 'TIME_FORMAT': 'iso-8601',
    # # 'TIME_INPUT_FORMATS': ['YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]', 'foobar789'],



