import os
import sys
from django.core.wsgi import get_wsgi_application

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Create WSGI application
application = get_wsgi_application()

# Vercel serverless handler
handler = application
