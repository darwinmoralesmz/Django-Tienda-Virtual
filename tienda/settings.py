import os
from pathlib import Path
import json
from django.utils.html import format_html



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
####datos de configuración
ruta= os.path.dirname(os.path.abspath(__file__))
f = open('{}/conf.json'.format(ruta), 'r')
conf_string = f.read()
f.close()
conf = json.loads(conf_string)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0xpyn45ol_6o9^zqv!^&fw_%e4g@mll=sz807^u*&79zmz3wi6'

BASE_URL=conf['base_url']
TOTAL_PAGINAS=conf['paginacion']

RUTA=conf['ruta']
RUTA2=conf['ruta2']
#envío mail
SERVER_STMP=conf['smtp']
PUERTO_SMTP= conf['smtp_puerto']
MAIL_SALIDA = conf['email']
PASSWORD_MAIL_SALIDA = conf['email_password']
WEBPAY_URL=conf['webpay_url']
WEBPAY_ID=conf['webpay_id']
WEBPAY_SECRET=conf['webpay_secret']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = conf['debug']

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home'
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

ROOT_URLCONF = 'tienda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'tienda.context_processors.categorias'
                
            ],
        },
    },
]

WSGI_APPLICATION = 'tienda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': conf['bd'],
        'USER': conf['user'],
        'PASSWORD': conf['password'],
        'HOST': conf['server'],
        'PORT': conf['puerto'],
        'OPTIONS': {
            'autocommit': True,

        },
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

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/assets/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}
