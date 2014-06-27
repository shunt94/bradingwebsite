__author__ = 'connor'
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASES= {
    'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': os.path.join('brading_db'),
         'USER': "connor",
     }
}
DEBUG=True
