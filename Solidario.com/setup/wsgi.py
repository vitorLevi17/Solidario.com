
import os
import sys


settings_path = '/home/Solidario/solidario.pythonanywhere.com/Solidario.com'
sys.path.insert(0, settings_path)


os.environ['DJANGO_SETTINGS_MODULE'] = 'setup.settings'


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
