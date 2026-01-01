import os, sys, shutil
from django.core.wsgi import get_wsgi_application

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

REPO_DB = os.path.join(PROJECT_ROOT, 'project_db.sqlite3')
TMP_DB = '/tmp/db.sqlite3'
try:
    if os.path.exists(REPO_DB) and not os.path.exists(TMP_DB):
        shutil.copy(REPO_DB, TMP_DB)
except Exception:
    pass

application = get_wsgi_application()
app = application