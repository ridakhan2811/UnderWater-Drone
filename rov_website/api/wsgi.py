import os
import sys
from django.core.wsgi import get_wsgi_application

# IMPORTANT: point to project root (rov_website)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
handler = application  # required by Vercel serverless
