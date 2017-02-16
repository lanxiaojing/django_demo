# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5edur$wlxns+m4ojq*fp6y&nij(#+1f$za@f!rojq-3snx=k&*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = ('django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'django.contrib.sites',
                  'raven.contrib.django.raven_compat',
                  "bootstrapform",
                  "account",
                  "fico863",
                  "gunicorn",)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "account.middleware.LocaleMiddleware",
    "account.middleware.TimezoneMiddleware",
)

ROOT_URLCONF = 'fico863.urls'

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

TEMPLATE_CONTEXT_PROCESSORS = [
    "account.context_processors.account",
]

WSGI_APPLICATION = 'fico863.wsgi.application'

USE_I18N = True

USE_L10N = True

USE_TZ = False

TIME_ZONE = 'Asia/Shanghai'
TIME_FORMAT = "H:i:s"
DATE_FORMAT = "Y-m-d"
DATETIME_FORMAT = "Y-m-d H:i:s"

LANGUAGE_CODE = 'zh.CN'

SITE_ID = 1

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(__file__), "static")

BASE_NUMBER = 5

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

ACCOUNT_LOGIN_REDIRECT_URL = "/upload"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_PASSWORD_CHANGE_REDIRECT_URL = "/account/login"
