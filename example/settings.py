# DEBUG = True

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'example.db'

SECRET_KEY = '-(izb-(l3wd$k7enthau^rj_eaze)!7h^_x=)hd#fs8!!i01+w'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'example.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'djangodblog',
    'django.contrib.admin',
)
