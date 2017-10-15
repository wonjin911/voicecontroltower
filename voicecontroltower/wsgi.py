"""
WSGI config for voicecontroltower project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "voicecontroltower.settings")
os.environ.setdefault("GOOGLE_APPLICATION_CREDENTIALS", "/home/svp_admin/workspace/voicecontroltower/voicecontrol/ekohacksvp-d7195ac866b4.json")

application = get_wsgi_application()
