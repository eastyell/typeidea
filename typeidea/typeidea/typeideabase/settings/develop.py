"""
this environment for development

"""

# 继承基类base
from .base import *
import os

DEBUG = True
# 开发数据库sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}