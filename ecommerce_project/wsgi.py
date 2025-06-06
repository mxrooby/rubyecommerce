"""
WSGI config for ecommerce_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv 
from django.core.wsgi import get_wsgi_application

# Load environment variables from .env
load_dotenv()  

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce_project.settings")

application = get_wsgi_application()
