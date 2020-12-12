from .base import *

DEBUG = True

ALLOWED_HOSTS = config('BOOKER_ALLOWED_HOSTS')

SECRET_KEY = config('BOOKER_SECRET_KEY')