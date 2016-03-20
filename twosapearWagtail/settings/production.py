from .base import *


DEBUG = False

SECRET_KEY = '0&-k88e%rjgqdy(#h_nr=sdf&)w&l2p7my+5t4i5s(-!vv#1('
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'twosapear.com']

try:
    from .local import *
except ImportError:
    pass
