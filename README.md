Welcome to BenchMap !

A demo is available here : https://benchmapapp.herokuapp.com/

This app is a map of rated benches.

The project is made with Python, Django, Js, HTML/CSS.  

If you want to use this project dont forget to update the database configuration in settings.py :

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bench',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}