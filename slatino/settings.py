from default_settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

MEDIA_APACHE_DIRECT = False

ADMINS = (
    ('admin name', 'admin@slatino.in.ua'),
)

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = "noreply@slatino.in.ua"

DATABASE_ENGINE = 'sqlite3'      # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ROOT_PATH + 'slatino_test'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
