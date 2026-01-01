import os
import sys
import shutil
from django.core.wsgi import get_wsgi_application

# Ensure project root is on Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

# Point Django to your settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# If you committed a prebuilt DB named project_db.sqlite3, copy it to /tmp on cold start
# so the runtime can open and write to it (ephemeral).
REPO_DB = os.path.join(PROJECT_ROOT, 'project_db.sqlite3')   # optional prebuilt DB in repo
TMP_DB = '/tmp/db.sqlite3'
try:
    if os.path.exists(REPO_DB) and not os.path.exists(TMP_DB):
        shutil.copy(REPO_DB, TMP_DB)
except Exception:
    # avoid crashing startup if copy fails; Django will create DB on migrate
    pass

# Create WSGI application and expose as `app` for Vercel
application = get_wsgi_application()
app = application