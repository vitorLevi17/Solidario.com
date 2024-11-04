import os
import sys


path = '/home/Solidario/solidario.pythonanywhere.com/Solidario.com'
if path not in sys.path:
    sys.path.append(path)


os.environ['DJANGO_SETTINGS_MODULE'] = 'Solidario.com.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
