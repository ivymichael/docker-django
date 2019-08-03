from split_settings.tools import optional, include
from os import environ
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV = environ.get("DJANGO_ENV") or "development"

base_settings = [
    "components/base.py",
    "components/database.py",
    "components/rq.py",
    "components/emails.py",
    "environments/%s.py" % ENV,
    optional("environments/local.py"),
]

include(*base_settings)
