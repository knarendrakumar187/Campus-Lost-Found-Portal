"""
URL Configuration for campus_portal project.

This file maps URLs (like /home, /login) to views (functions that handle requests).
Think of it as a "table of contents" for your website.
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    # Admin panel URL - accessible at /admin/
    path('admin/', admin.site.urls),
    
    # All URLs from lostfound app
    # When someone visits /, Django will look in lostfound/urls.py
    path('', include('lostfound.urls')),

    # Serve media files in production (Hackathon specific config)
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

# Serve static files during development if needed (WhiteNoise handles this in prod)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

