"""
Django settings for campus_portal project.

This file contains all the configuration for your Django project.
Think of it as the "control center" for your application.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR is the root folder of your project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# This key is used to encrypt passwords and sessions
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-this-in-production-12345')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True shows detailed error pages (good for development)
# DEBUG = False hides errors (good for production)
DEBUG = 'RENDER' not in os.environ

# ALLOWED_HOSTS: Which domains can access your site
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition
# INSTALLED_APPS: All the apps (modules) your project uses
INSTALLED_APPS = [
    'django.contrib.admin',        # Admin panel (built-in)
    'django.contrib.auth',         # User authentication (built-in)
    'django.contrib.contenttypes',  # Content types framework (built-in)
    'django.contrib.sessions',      # Session management (built-in)
    'django.contrib.messages',      # Flash messages (built-in)
    'django.contrib.staticfiles',   # Static files (CSS, JS, images)
    'lostfound',                    # Our custom app for lost & found items
]

# MIDDLEWARE: Components that process requests/responses
# They run in order (top to bottom)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Protects against CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Adds user to request
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT_URLCONF: Where Django looks for URL patterns
ROOT_URLCONF = 'campus_portal.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Where to find HTML templates
        'APP_DIRS': True,  # Also look in each app's templates folder
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',  # Adds 'user' to templates
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'campus_portal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# SQLite is perfect for beginners - it's a file-based database
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# SQLite is perfect for beginners - it's a file-based database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Render PostgreSQL Database Configuration
import dj_database_url
database_url = os.environ.get('DATABASE_URL')

if database_url:
    DATABASES['default'] = dj_database_url.parse(
        database_url,
        conn_max_age=600,
        conn_health_checks=True,
    )


# Password validation
# Rules for password strength
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
# Language and timezone settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Where to find static files during development
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (User uploaded files like images)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Where uploaded files are stored

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login URLs - where to redirect after login/logout
LOGIN_URL = 'login'  # If user tries to access protected page, redirect here
LOGIN_REDIRECT_URL = 'home'  # After login, go to home page
LOGOUT_REDIRECT_URL = 'home'  # After logout, go to home page

