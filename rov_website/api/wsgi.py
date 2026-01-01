import os
import sys
from django.core.wsgi import get_wsgi_application

# Ensure project root is on Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

# Point Django to your settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Create WSGI application
application = get_wsgi_application()

# Expose it as `app` for Vercel
app = application