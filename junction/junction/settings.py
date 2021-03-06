import os

from django.conf.global_settings import *  # noqa

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

CORE_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.webdesign',
)

THIRD_PARTY_APPS = (
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',

    'django_extensions',

    'bootstrap3',

    'pagedown',
    'django_markdown',
)

OUR_APPS = (
    'conferences',
    'proposals',
    'pages',
)

INSTALLED_APPS = CORE_APPS + THIRD_PARTY_APPS + OUR_APPS

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend"
)

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[Junction] "
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
LOGIN_REDIRECT_URL = '/'

# E-Mail Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', ''),
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', ''),
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Junction <noreply@pssi.org.in>'

BOOTSTRAP3 = {
    'required_css_class': 'required',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },

    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', ],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['file', ],
        },
    }
}


ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'junction.wsgi.application'

TIME_ZONE = 'Asia/Kolkata'
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets', 'collected-static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets', 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', ''),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': os.environ.get('DB_PORT', ''),
    }
}

ADMINS = (
    ('Bibhas', 'me@bibhas.in'),
    ('Kracekumar', 'me@kracekumar.com'),
    ('Sivabramaniam Arunachalam', 'siva@sivaa.in'),
)


SECRET_KEY = os.environ.get('SECRET_KEY', 'z^bd9lk)o!03n#9e_u87zidd1zt7*^_oc4v6t!@@86vtbu0*&j')

DEBUG = TEMPLATE_DEBUG = os.environ.get('DEBUG', 'on') == 'on'

ALLOWED_HOSTS = []  # TODO:

# Dev Settings

try:
    from junction.dev import *  # noqa
    from junction.prod import *  # noqa
except ImportError:
    pass
