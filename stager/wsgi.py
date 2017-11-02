"""
WSGI config for stager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stager.settings")

application = get_wsgi_application()
<<<<<<< HEAD
application = DjangoWhiteNoise(application)
=======
application = DjangoWhiteNoise(application)
>>>>>>> 76496ebe1affab8e182d30402b6d889271da3fbc
