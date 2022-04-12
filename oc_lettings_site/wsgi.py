import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
sys.path.append('home/myname/My-Project/app')

application = get_wsgi_application()
