"""
URL Configuration for campus_portal project.

This file maps URLs (like /home, /login) to views (functions that handle requests).
Think of it as a "table of contents" for your website.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin panel URL - accessible at /admin/
    path('admin/', admin.site.urls),
    
    # All URLs from lostfound app
    # When someone visits /, Django will look in lostfound/urls.py
    path('', include('lostfound.urls')),
]

# Serve media files during development
# This allows uploaded images to be displayed
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

