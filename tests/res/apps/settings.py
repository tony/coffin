from os import path


DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.sqlite3",
    }
}

INSTALLED_APPS = (
    'templatelibs_app',
    'feeds_app',
    'urls_app',
)

DEBUG=True
CACHES=None

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.filesystem.load_template_source',
)

TEMPLATE_DIRS = (path.join(path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'
SECRET_KEY = 'testing123'
DEFAULT_INDEX_TABLESPACE=''
