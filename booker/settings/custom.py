from .base import *

DEBUG = config('BOOKER_DEBUG')

ALLOWED_HOSTS = config('BOOKER_ALLOWED_HOSTS')

SECRET_KEY = config('BOOKER_SECRET_KEY')