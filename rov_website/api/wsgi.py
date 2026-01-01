import os
import sys
from django.core.wsgi import get_wsgi_application  # This is ALWAYS correct

# Point to your project root (rov_website)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

# Tell Django where the settings are
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Standard Django WSGI application
application = get_wsgi_application()

# Required for Vercel serverless
handler = application
