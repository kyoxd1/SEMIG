from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER' : 'postgres',
        'PASSWORD' : 'b79VVMkmkFGjx7jbwxlf',
        'HOST' : 'containers-us-west-127.railway.app',
        'PORT' : '5585',   
    }
}