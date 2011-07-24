import os

ROOT_PATH = os.path.dirname(__file__) + '/'
SITE_PATH = os.path.normpath(os.path.join(ROOT_PATH, '../')) + '/'
LIB_PATH = os.path.join(SITE_PATH, 'libs')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('dixon', 'dixon.che@gmail.com'),
)

MANAGERS = ADMINS

AUTH_USER_EMAIL_UNIQUE = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

DEFAULT_FROM_EMAIL = "noreply@slatino.in.ua"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',      # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',             # Or path to database file if using sqlite3.
        'USER': '',             # Not used with sqlite3.
        'PASSWORD': '',         # Not used with sqlite3.
        'HOST': '',             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': ''             # Set to empty string for default. Not used with sqlite3.
    }
}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
#TIME_ZONE = 'Ukraine/Kiev'

_ = lambda s: s

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russion')),
    ('uk', _('Ukrainian')),
)

#DEFAULT_CHARSET = 'utf-8'

DEFAULT_LANG = 'ru'
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = SITE_PATH + 'media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'psf$&om-eto3yo&i5k8i5kyde+o_hf4!k#*#&24iqsp+y9luwc'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "slatino.context_processors.person_processor",
    "django.core.context_processors.media",
    )

MIDDLEWARE_CLASSES = (
    
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'annoying.middlewares.RedirectMiddleware',
)

ROOT_URLCONF = 'slatino.urls'

TEMPLATE_DIRS = (
    ROOT_PATH + "templates",
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.messages',
    'slatino.apps.Links',
    'slatino.apps.Gallery',
    'slatino.apps.Persons',
    'slatino.apps.Institute',
    'slatino.apps.Telephone',
    'slatino.apps.Publications',
    'slatino.apps.Transport',
    'slatino.apps.Profile',
    'slatino.apps.Tagsfield',
    'registration',
    'publicauth',
)

AUTH_PROFILE_MODULE = 'Profile.UserProfile'

PUBLICATION_LAST_COUNT = 5
PUBLICATION_PER_PAGE = 10

ACCOUNT_ACTIVATION_DAYS = 2

AUTHENTICATION_BACKENDS = ( 'publicauth.PublicBackend',)
VKONTAKTE_APP_ID = 2417923
VKONTAKTE_API_KEY = "XXXX"
VKONTAKTE_SECRET_KEY = "eZUSJg2WnvsXWIx4lt6Q"

TAGS_URL = "/tag/%s/"

POST_TYPES = (
    ('article', _('Article')),
    ('news', _('News')),
    ('blogpost', _('Blogpost')),
)

CAPTCHA_REFRESH_LINK_TEXT = _("Refresh code")
CAPTCHA_SIZE = (80, 14)
CAPTCHA_REFRESH = True
