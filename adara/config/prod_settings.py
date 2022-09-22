import os

# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-dnfca5yq*g)*y3^j#2&(7wb+@u4!)4=w$c#c33qk0b36tmq+tn'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shop_db',
        'USER': 'tixon',
        'PASSWORD': '111',
        'HOST': 'localhost',
        'PORT': '',
    }
}


STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')