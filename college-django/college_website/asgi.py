import os
from django.core.asgi import get_asgi_application

# Set the default settings module for your project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college_website.settings')

# Get the ASGI application callable to be used by ASGI servers
application = get_asgi_application()
