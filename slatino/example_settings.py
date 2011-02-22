from default_settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

MEDIA_APACHE_DIRECT = False

ADMINS = (
    ('admin name', 'admin@slatino.in.ua'),
)

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = "noreply@slatino.in.ua"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',      # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': ROOT_PATH + 'slatino_test',             # Or path to database file if using sqlite3.
        'USER': '',             # Not used with sqlite3.
        'PASSWORD': ''         # Not used with sqlite3.
    }
}
