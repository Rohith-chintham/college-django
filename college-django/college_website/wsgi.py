import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'college_website' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college_website.settings')

# Get the WSGI application callable to be used by WSGI servers
application = get_wsgi_application()
