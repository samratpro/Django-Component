# Setting ------------------------------------------

# App connection..     # Probbaly 33 line
INSTALLED_APPS = [
    'NewApp',
]

# Static File Connection..   # Probbaly 123 line
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Postgresql database  # Probbaly 78 line
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'samrat',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
    }
}


# Template Connection..
DIRS': [BASE_DIR / 'templates'], # Probbaly 59 line
