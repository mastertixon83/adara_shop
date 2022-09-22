import os
from typing import List

# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-dnfca5yq*g)*y3^j#2&(7wb+@u4!)4=w$c#c33qk0b36tmq+tn'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

INTERNAL_IPS = [
    "127.0.0.1",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shop_db',
        'USER': 'tixon',
        'PASSWORD': 'gft654gfhgf',
        'HOST': '192.168.56.12',
        'PORT': '5432',
    }
}

STATIC_DIR = os.path.join(BASE_DIR, '/static/')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'shop'),
# ]
