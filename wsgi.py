import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'fadles.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
