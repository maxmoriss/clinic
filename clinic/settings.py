"""
Django settings for clinic project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# Basic application settings and paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORE_PATH = os.path.realpath(os.path.dirname(__file__))
BASE_APP_NAME = 'clinic'
SITE_URL = ''
SECRET_KEY = 'g-6ot^5z5!0x5n@00hxa)ffzylft4d!$kl9c!qo%=x=m%1s9vh'
SITE_ID = 1
DEBUG = True
ROOT_URLCONF = '%s.urls' % BASE_APP_NAME
WSGI_APPLICATION = '%s.wsgi.application' % BASE_APP_NAME
ALLOWED_HOSTS = ['*']
ADMINS = (
    ('Max Morozov', 'maxmoriss@gmail.com'),
)

# Internationalization
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Media & static directories
# STATICFILES_FINDERS = STATICFILES_FINDERS + (
#     'compressor.finders.CompressorFinder',
# )
STATICFILES_DIRS = (os.path.join(CORE_PATH, 'static'),)
STATIC_ROOT = os.path.join(CORE_PATH, 'collected_static')
MEDIA_ROOT = os.path.join(CORE_PATH, 'media_dev' if DEBUG else 'media')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Application definition
INSTALLED_APPS = (
    # django suit
    'suit',

    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # site applications
    'core',
)

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

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

# admin menu
SUIT_CONFIG = {
    'ADMIN_NAME': u'Поликлиника',
    'HEADER_DATE_FORMAT': 'l, j E Y',
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': False,
    'LIST_PER_PAGE': 30,
    'MENU': (
        {
            'label': u'Записи на прием',
            'app': 'core',
            'icon': 'icon-book'
        },
    )
}

# shitty debug features
if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
    )

# other site settings
ENTRY_HOURS = [9, 10, 11, 12, 13, 14, 15, 16, 17]

# Load production settings (if exists)
try:
    from settings_production import *
except ImportError:
    pass