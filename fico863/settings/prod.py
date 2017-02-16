# encoding=utf-8

from common import *
import os

DEBUG = False

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        "LOCATION": "10.44.31.233:11211",
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fico',
        'USER': 'dev',
        'PASSWORD': 'dev012131',
        'HOST': 'rdsxcz5wl9f88rs5961i.mysql.rds.aliyuncs.com',
        'PORT': '',
    }
}

EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'robot@princetechs.com'
EMAIL_HOST_PASSWORD = 'Robot0023'
USE_TLS = True


APP_HOST = "fico.princetechs.com"


STATIC_ROOT = os.path.join(os.path.dirname(__file__), "../static")


RAVEN_CONFIG = {
    'dsn': 'http://06296f5d2cf14d61987fce22b99296b6:3be59b5a8e584f3d9b5ab33cd389db64@sentry.princetechs.com//11',
}


ALLOWED_HOSTS = ["fico.princetechs.com"]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format':
            '%(levelname)s %(asctime)s %(pathname)s:%(lineno)d:: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename':
            os.path.join("/home/web_log/fico863/", "fico863.pro.log"),
            'backupCount': 24,
            'formatter': 'verbose',
            'level': 'WARN',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'WARN',
        },
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'WARN',
            'propagate': True,
        },
    }
}
