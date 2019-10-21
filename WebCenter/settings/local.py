# _*_coding:utf-8_*_

# write_author :chenzhengwei

# write_date :2019/10/21 上午10:20

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webcenter',
        'USER': 'root',
        'PASSWORD': 'chenzwcc',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')

]
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')