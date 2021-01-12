"""
WSGI config for reactor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reactor.settings')

_application = get_wsgi_application()


env_variables_to_pass = ['SECRET_KEY', 'DB_NAME',
                         'DB_USERNAME', 'DB_PASSWORD',
                         'DB_HOSTNAME', 'DB_PORT',
                         'ENVIRONMENT', 'AWS_KEY_ID',
                         'AWS_SECRET_KEY', 'AWS_BUCKET',
                         'AWS_REGION', 'SENDGRID_API_KEY',
                         'MEASUREMENT_ID']


def application(environ, start_response):
    # pass the WSGI environment variables on through to os.environ
    for var in env_variables_to_pass:
        os.environ[var] = environ.get(var, '')
    return _application(environ, start_response)
