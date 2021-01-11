"""
WSGI config for reactor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

_application = get_wsgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reactor.settings')

env_variables_to_pass = ['SECRET_KEY', 'DB_NAME',
                         'DB_USERNAME', 'DB_PASSWORD',
                         'DB_HOSTNAME', 'DB_PORT']


def application(environ, start_response):
    # pass the WSGI environment variables on through to os.environ
    for var in env_variables_to_pass:
        os.environ[var] = environ.get(var, '')
    return _application(environ, start_response)
