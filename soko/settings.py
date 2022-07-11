"""
Django settings for soko project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dkzq6i))!f$0+@f=2ldv$hos^ye#!b!-zicjc8c1dgm1+q=iss'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ALLOWED_HOSTS = []
# The Mpesa environment to use
# Possible values: sandbox, production

MPESA_ENVIRONMENT = 'sandbox'

# Credentials for the daraja app

MPESA_CONSUMER_KEY = config('MPESA_CONSUMER_KEY')
MPESA_CONSUMER_SECRET = config('MPESA_CONSUMER_SECRET')

#Shortcode to use for transactions. For sandbox  use the Shortcode 1 provided on test credentials page

MPESA_SHORTCODE = config('MPESA_SHORTCODE')

# Shortcode to use for Lipa na MPESA Online (MPESA Express) transactions
# This is only used on sandbox, do not set this variable in production
# For sandbox use the Lipa na MPESA Online Shorcode provided on test credentials page

MPESA_EXPRESS_SHORTCODE = config('MPESA_EXPRESS_SHORTCODE')

# Type of shortcode
# Possible values:
# - paybill (For Paybill)
# - till_number (For Buy Goods Till Number)

MPESA_SHORTCODE_TYPE = config('MPESA_SHORTCODE_TYPE')

# Lipa na MPESA Online passkey
# Sandbox passkey is available on test credentials page
# Production passkey is sent via email once you go live

MPESA_PASSKEY = config('MPESA_PASSKEY')

# Username for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_USERNAME = config('MPESA_INITIATOR_USERNAME')

# Plaintext password for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_SECURITY_CREDENTIAL = config('MPESA_INITIATOR_SECURITY_CREDENTIAL')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'django.contrib.sites',
    'allauth_ui',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'widget_tweaks',
    'django_daraja',
    'shop',
    'users',
    'crispy_forms',
    'crispy_bootstrap5',
]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'soko.urls'

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

WSGI_APPLICATION = 'soko.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTHENTICATION_BACKENDS = [
 
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]


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

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

cloudinary.config( 
  cloud_name = config('CLOUD_NAME'), 
  api_key = config('CLOUDINARY_API'), 
  api_secret = config('CLOUDINARY_SECRET') 
)

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGIN_REDIRECT_URL = 'homepage'

#django-allauth registraion settings
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =1
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_SIGNUP_REDIRECT_URL = '/accounts/login/'
# 1 day
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400

#or any other page
ACCOUNT_LOGOUT_REDIRECT_URL ='/accounts/login/'

# redirects to profile page if not configured.
LOGIN_REDIRECT_URL = 'homepage'
LOGIN_URL = '/accounts/login/'