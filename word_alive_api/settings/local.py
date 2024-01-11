from .base import *
from .base import env 

DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='django-insecure-yb3xsou3%7np*oaev*1ir%o-56z$uypzk-vcc%j7!rnjk((f%a')

ALLOWED_HOSTS = ['localhost','0.0.0.0', '127.0.0.1']
