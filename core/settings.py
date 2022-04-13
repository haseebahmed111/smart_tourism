import os
from decouple import config
from unipath import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# load production server from .env
ALLOWED_HOSTS = ['localhost', 'localhost:85', '127.0.0.1', 'smarttourismfast.herokuapp.com',
                 config('SERVER', default='127.0.0.1')]
CSRF_TRUSTED_ORIGINS = ['http://localhost:85', 'http://127.0.0.1', 'https://smarttourismfast.herokuapp.com',
                        'https://' + config('SERVER', default='127.0.0.1')]

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.home',  # Enable the inner home (home)
    'tour_guide',
    'car_vendor',
    'trip_vendor',
    'management',
    'user_dashboard'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"  # Route defined in home/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in home/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'apps/static'),
)
if 'DATABASE_URL' in os.environ:
    import dj_database_url

    DATABASES = {'default': dj_database_url.config()}

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Smart Tourism Admin",

    # # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or
    # None)
    "site_header": "Smart Tourism",

    # # Logo to use for your site, must be present in static files, used for brand on top left
    # "site_logo": "assets/img/logo.png",

    # # CSS classes that are applied to the logo above
    # "site_logo_classes": "img-circle",

    # # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    # "site_icon": None,

    # # Welcome text on the login screen
    # "welcome_sign": "Welcome to the library",

    # # Copyright on the footer
    "copyright": "Smart Tourism",

    # # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",

    # # Field name on user model that contains avatar image
    "user_avatar": None,

    # ############
    # # Top Menu #
    # ############

    # # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Admin Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Smart Tourism Home", "url": "home"},
        # # external url that opens in a new window (Permissions can be added)
        # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        #
        # # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        #
        # # App with dropdown menu to all its models pages (Permissions checked against models)
        # {"app": "books"},
    ],

    # #############
    # # User Menu #
    # #############

    # # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    # "usermenu_links": [
    #     {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
    #     {"model": "auth.user"}
    # ],

    # #############
    # # Side Menu #
    # #############

    # # Whether to display the side menu
    "show_sidebar": True,

    # # Whether to aut expand the menu
    "navigation_expanded": True,

    # # Hide these apps when generating side menu e.g (auth)
    # "hide_apps": [],

    # # Hide these models when generating side menu (e.g auth.user)
    # "hide_models": [],

    # # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    # "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # # Custom links to append to app groups, keyed on app name

    # # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,
    # 5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,
    # 5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,
    # 5.4.2 # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    # #################
    # # Related Modal #
    # #################
    # # Use modals instead of popups
    "related_modal_active": True,

    # #############
    # # UI Tweaks #
    # #############

    # # Relative paths to custom CSS/JS scripts (must be present in static files)
    # "custom_css": "/dashboard_assets/css/black-dashboard.css",
    # "custom_js": "/dashboard_assets/js/core/jquery.min.js",
    # # Whether to show the UI customizer on the sidebar
    # "show_ui_builder": True,

    # ###############
    # # Change view #
    # ###############
    # # Render out the change view as a single form, or in tabs, current options are
    # # - single
    # # - horizontal_tabs (default)
    # # - vertical_tabs
    # # - collapsible
    # # - carousel
    # "changeform_format": "horizontal_tabs",
    # # override change forms on a per modeladmin basis
    # "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # # Add a language dropdown into the admin
    # "language_chooser": True,

}

JAZZMIN_UI_TWEAKS = {
    # "theme": "yeti",
}
