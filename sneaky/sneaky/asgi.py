import os
import django
from channels.routing import get_default_application
os.environ.setdefault("DJANDO_SETTINGS_MODULE","sneaky.settings")
django.setup()
application=get_default_application()