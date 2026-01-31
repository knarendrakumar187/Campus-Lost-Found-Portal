"""
Script to create a superuser non-interactively.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campus_portal.settings')
django.setup()

from django.contrib.auth.models import User

# Check if admin user already exists
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@campus.edu',
        password='admin123'
    )
    print("Superuser created successfully!")
    print("   Username: admin")
    print("   Password: admin123")
else:
    print("Admin user already exists!")

