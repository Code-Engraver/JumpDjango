from .base import *

ALLOWED_HOSTS = ['3.34.55.126']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': '$NF0zw:pZO0O.aG.}6M_df2a;t{rk&MQ',
        'HOST': 'ls-66d1dfa585e494051b783525bd9421ffdb65cf45.cvoruco8lzz0.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432'
    }
}
