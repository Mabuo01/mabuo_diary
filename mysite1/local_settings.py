import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'django-insecure-i#^60kom&v5akh8u%nacki7=wl0uf=#^2t*-_-fz0t!ly=g29n'

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'TEST': {
            'NAME': 'mytestdb',
        }}
}
DEBUG = True