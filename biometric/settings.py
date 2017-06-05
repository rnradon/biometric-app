"""
Django settings for biometric project.

Generated by 'django-admin startproject' using Django 1.11.dev20161121173054.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$%nc2#k515u*-9+77beo*#_x2b-@=6x$m)(54@b9x^ot61^sh^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'biometric-app.herokuapp.com',
    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_auth',
    'rest_framework.authtoken',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'phonenumber_field',
    'scanapp',
]

SITE_ID = 1

REST_FRAMEWORK = { 
   
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication', 
        # 'rest_framework.authentication.SessionAuthentication',
        
    ), 

    'DEFAULT_MODEL_SERIALIZER_CLASS': 
        'rest_framework.serializers.ModelSerializer', 

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    )


} 

REST_AUTH_SERIALIZERS = {
    # 'LOGIN_SERIALIZER': 'scanapp.serializers.LoginSerializer',
    # 'PASSWORD_RESET_SERIALIZER': 'scanapp.serializers.PasswordSerializer',
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'scanapp.serializers.RegisterSerializer',

}

REST_SESSION_LOGIN = False

ACCOUNT_AUTHENTICATION_METHOD = 'username',   
ACCOUNT_EMAIL_REQUIRED = False,
ACCOUNT_USERNAME_REQUIRED = True,
ACCOUNT_USER_MODEL_EMAIL_FIELD = None


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]

ROOT_URLCONF = 'biometric.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'biometric.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'biometric_app',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD':'123',
        'PORT':3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/


PHONENUMBER_DEFAULT_REGION = 'IN'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "rnradon17@gmail.com"
EMAIL_HOST_PASSWORD = "gnkbphqrqhilxctl"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

TWILIO_ACCOUNT_SID = 'AC17c5c823570dc4c8e5637d742dfd9e0d'
TWILIO_AUTH_TOKEN = 'e8b81c5f8c2378223b084d853efebbde'

SENDSMS_BACKEND = 'myapp.mysmsbackend.SmsBackend'



MSG91_AUTHKEY = '154618AwWLYscrj593050fe'
MSG91_ROUTE = '4'