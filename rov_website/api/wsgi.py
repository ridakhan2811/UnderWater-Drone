import os
import sys
from django.core.wsgi import get_wsgi_application

# Point to project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

# Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# WSGI application
application = get_wsgi_application()

# Vercel expects a handler variable
handler = application
