# prueba_impacte

Durante el proceso instale en mi entorno djangorestframework, django-cors-headers, bootstrap y axios.

    python -m pip install djangorestframework
    
    python -m pip install django-cors-headers
    
    npm install bootstrap-vue
    
    npm install axios

Ademas es necesario crear la conexion con PostgreSQL

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'impacte',
        'USER': 'victor',
        'PASSWORD': 'victor',
        'HOST': 'localhost',
        'DATABASE_PORT': '5432',
    }
}
