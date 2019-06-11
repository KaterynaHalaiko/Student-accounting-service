### WARNING!: do not keep this file in repository;
### create it from sample_env_setting.py every time on every new
### server and fill in proper settings for that new environment

### Do not modify next 2 lines
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

### You can modify below settings:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'students_db_user',
        'PASSWORD': 'password',
        'NAME': 'students_db',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '199fen&^3znb^90m(=2)3iwu-o7w8u=u1cslg8xdxawebojdjf'

# website root url
PORTAL_URL = 'http://students.vitaliypodoba.com'

# email settings
ADMIN_EMAIL = 'admin@students.vitaliypodoba.com'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'vitaliypodoba@gmail.com'
EMAIL_HOST_PASSWORD = '********'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'students.vitaliypodoba.com']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = '/path/to/folder/with/static/files/'

# media files
MEDIA_URL = '/media/'
MEDIA_ROOT = '/path/to/folder/with/media/files/'

# facebook API Keys
SOCIAL_AUTH_FACEBOOK_KEY = '**********'
SOCIAL_AUTH_FACEBOOK_SECRET = '***********************'

# admins
ADMINS = (('Vitaliy', 'vitaliypodoba@gmail.com'),)
MANAGERS = (('Manager', 'manager@gmail.com'),)
