from .base import *


SECRET_KEY = 'django-insecure-ut!4#31wyu0-r#3st(l3@u84=p@x9kad50e808ek7ho%dgib-3'

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'library',
        'USER': 'IvanT',
        'PASSWORD': 'qwaszx',
        'HOST': 'db',
        'PORT': '5432',
    }
}
