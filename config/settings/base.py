from pathlib import Path
from config.env import env

BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # packages
    'drf_yasg',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    # apps
    'core.apps.accounts',
    'core.apps.orders',
    'core.apps.common',
    'core.apps.payment',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': env.str('POSTGRES_HOST'),
        'PORT': env.str('POSTGRES_PORT'),
    }
}



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




LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = False


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'resources/static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'resources/media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'

EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
EMAIL_BACKEND = env.str('EMAIL_BACKEND')
EMAIL_HOST = env.str('EMAIL_HOST')
EMAIL_PORT = env.str('EMAIL_PORT')
EMAIL_USE_TLS = env.str('EMAIL_USE_TLS')

from config.conf import *

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
LANGUAGES = (
    ('uz', 'Uzbek'),
    ('en', 'English'),
    ('ru', 'Russian'),
)   
MODELTRANSLATION_LANGUAGES = ('uz', 'en', 'ru')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', env.str("SWAGGER_PROTOCOL", 'https'))

CORS_ALLOW_ALL_ORIGINS = True


CSRF_TRUSTED_ORIGINS = [
    "https://acargo.felixits.uz",
    'http://localhost:8002',
    'http://127.0.0.1:8002',
]

ALLOWED_ATMOS_IPS = []
CONSUMER_KEY = env.str('CONSUMER_KEY')
CONSUMER_SECRET = env.str('CONSUMER_SECRET')
STORE_ID = env.str('STORE_ID')
API_KEY = env.str('API_KEY')