"""
Django settings for RupseOnline project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i3jrp$h-yskvh6x-kio)$jf35x9gp*eg-(vg5-vgk+&ytii1!n'


ALLOWED_HOSTS = '*'


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)



# reading .env file
environ.Env.read_env()


# False if not in os.environ
DEBUG = env('DEBUG')


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'material.admin',
    'material.admin.default',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'django.contrib.sites',  # can be used later
    'allauth',
    'allauth.account',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount', #can be used later
    'rest_auth.registration',
    'django_filters',
    'django_extensions',
    'rangefilter',
    'taggit',
    'taggit_serializer',
    'ckeditor',
    'ckeditor_uploader',
    'imagekit',

    #custom apps
    'apps.accounts',
    'apps.products',
    'apps.orders',
    'apps.contacts',
]

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     # 'whitenoise.middleware.WhiteNoiseMiddleware',

]

CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = (
#     "https://localhost:3000",
#     "http://localhost:3000",
#     "http://rupseonline.aakashlabs.com",
#     "https://front.rupseonline.com",
#
# )

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

ROOT_URLCONF = 'RupseOnline.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'RupseOnline.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
   # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
    # read os.environ['SQLITE_URL']
    'extra': env.db('SQLITE_URL', default='sqlite:////tmp/my-tmp-sqlite.db')
}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

CKEDITOR_UPLOAD_PATH = "uploads/"

#ckeditor configs # todo
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'width': 1000,
        'height': 400
    },
}

AUTH_USER_MODEL = 'accounts.CustomUser'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

REST_FRAMEWORK = {
    # 'DEFAULT_PARSER_CLASSES': (
    #         'rest_framework.parsers.JSONParser',
    #         'rest_framework.parsers.FormParser',
    #     ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # # 'DEFAULT_PAGINATION_CLASS': 'RupseOnline.core.pagination.CustomPagination',
    'PAGE_SIZE': 15,
}
# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
# ACCOUNT_SESSION_REMEMBER = True
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_UNIQUE_EMAIL = True
#
# REST_AUTH_SERIALIZERS = {
#     'USER_DETAILS_SERIALIZER': 'apps.accounts.api.serializers.CustomUserDetailsSerializer',
#     'LOGIN_SERIALIZER': 'apps.accounts.api.serializers.CustomLoginSerializer',
# }
#
# REST_AUTH_REGISTER_SERIALIZERS = {
#     "REGISTER_SERIALIZER": "apps.accounts.api.serializers.CustomRegisterSerializer",
# }

ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =10
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQURIED=True
#ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 115
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400 # 1 day in seconds
SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_EMAIL_REQUIRED = ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_STORE_TOKENS=True
LOGIN_REDIRECT_URL = '/'
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            # 'first_name',
            # 'last_name',
            # 'verified',
            # 'locale',
            # 'timezone',
            # 'link',
            # 'gender',
            # 'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.12',
    },
     'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# REST_USE_JWT = True

MATERIAL_ADMIN_SITE = {
    'SHOW_COUNTS': True,
}

# SMTP Mail service with decouple
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tech.aakashlabs@gmail.com'
SERVER_EMAIL = 'tech.aakashlabs@gmail.com'
# EMAIL_HOST_PASSWORD = 'ovlpoqdkuiktqfki'
EMAIL_HOST_PASSWORD = 'Labs@123'
EMAIL_USE_TLS = True
EMAIL_USE_SLS = False
EMAIL_PORT = 587
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

#credentials
#981-3488228
#saroj.aakashlabs@gmail.com
#2000-01-01


# class SocialAccountAdapter(DefaultSocialAccountAdapter):
#     def authentication_error(self, request, provider_id, error, exception, extra_context):
#         your_log_function(
#             'SocialAccount authentication error!',
#             'error',
#             request,
#             extra_data = {'provider_id': provider_id, 'error': error.__str__(), 'exception': exception.__str__(), 'extra_context': extra_context},
#         )