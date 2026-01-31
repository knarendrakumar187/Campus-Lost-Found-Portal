"""
Script to create test data for Lost & Found Portal
Run this to populate the database with sample items
"""

import os
import django
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campus_portal.settings')
django.setup()

from django.contrib.auth.models import User
from lostfound.models import LostItem, FoundItem

# Get or create a test user
user, created = User.objects.get_or_create(
    username='testuser',
    defaults={
        'email': 'test@campus.edu',
        'first_name': 'Test',
        'last_name': 'User'
    }
)
if created:
    user.set_password('test123')
    user.save()
    print(f"Created test user: {user.username}")

# Sample Lost Items Data
lost_items_data = [
    {
        'title': 'Lost iPhone 13 Pro',
        'description': 'Lost my iPhone 13 Pro with a black case. Has a crack on the screen. Last seen in the library on 2nd floor. Please contact if found!',
        'category': 'electronics',
        'location_lost': 'Library, 2nd Floor, Study Room 205',
        'date_lost': date.today() - timedelta(days=2),
        'contact_info': 'Phone: 9876543210, Email: student@campus.edu',
        'status': 'pending',
        'is_approved': True
    },
    {
        'title': 'Lost Black Wallet',
        'description': 'Lost my black leather wallet containing ID card, credit cards, and some cash. Has my student ID inside.',
        'category': 'accessories',
        'location_lost': 'Cafeteria, near the entrance',
        'date_lost': date.today() - timedelta(days=5),
        'contact_info': 'Phone: 9876543211',
        'status': 'pending',
        'is_approved': True
    },
    {
        'title': 'Lost Blue Backpack',
        'description': 'Lost my blue Nike backpack with laptop, books, and notebooks inside. Very important for my studies!',
        'category': 'accessories',
        'location_lost': 'Computer Lab, Building A, Room 301',
        'date_lost': date.today() - timedelta(days=1),
        'contact_info': 'Email: urgent@campus.edu, Phone: 9876543212',
        'status': 'pending',
        'is_approved': True
    },
    {
        'title': 'Lost Mathematics Textbook',
        'description': 'Lost my Calculus textbook. It\'s a thick blue book with "Calculus Early Transcendentals" written on it.',
        'category': 'books',
        'location_lost': 'Mathematics Department, 3rd Floor',
        'date_lost': date.today() - timedelta(days=3),
        'contact_info': 'Phone: 9876543213',
        'status': 'pending',
        'is_approved': True
    },
    {
        'title': 'Lost AirPods Pro',
        'description': 'Lost my white AirPods Pro in a black case. Last used in the gym during morning workout.',
        'category': 'electronics',
        'location_lost': 'Gymnasium, Locker Room Area',
        'date_lost': date.today() - timedelta(days=4),
        'contact_info': 'Phone: 9876543214',
        'status': 'pending',
        'is_approved': True
    },
    {
        'title': 'Lost Student ID Card',
        'description': 'Lost my student ID card. Name: John Doe, ID: STU2024001. Please return if found.',
        'category': 'documents',
        'location_lost': 'Administration Building, Ground Floor',
        'date_lost': date.today() - timedelta(days=1),
        'contact_info': 'Email: john.doe@campus.edu',
        'status': 'pending',
        'is_approved': True
    }
]

# Sample Found Items Data
found_items_data = [
    {
        'title': 'Found Black Wallet',
        'description': 'Found a black leather wallet near the cafeteria entrance. Contains ID card and some cards inside.',
        'category': 'accessories',
        'location_found': 'Cafeteria, Main Entrance',
        'date_found': date.today() - timedelta(days=4),
        'contact_info': 'Phone: 9876543220, Email: finder@campus.edu',
        'status': 'pending',
        'is_approved': True
    },
    {
        'title': 'Found Blue Water Bottle',
        'description': 'Found a blue stainless steel water bottle in the library. Has some stickers on it.',
        'category': 'accessories',
        'location_found': 'Library, Reading Area, 1st Floor',
        'date_found': date.today() - timedelta(days=2),
        'contact_info': 'Phone: 9876543221',
        'status': 'pending',
        'is_approved': True
    },
    {
        'title': 'Found Red Laptop Charger',
        'description': 'Found a red laptop charger (USB-C) in the computer lab. Looks like it belongs to a MacBook.',
        'category': 'electronics',
        'location_found': 'Computer Lab, Building A, Room 301',
        'date_found': date.today() - timedelta(days=1),
        'contact_info': 'Email: charger@campus.edu',
        'status': 'pending',
        'is_approved': True
    },
    {
        'title': 'Found Set of Keys',
        'description': 'Found a set of keys with a car key fob and several house keys. Found near the parking lot.',
        'category': 'accessories',
        'location_found': 'Parking Lot, Near Building B',
        'date_found': date.today() - timedelta(days=3),
        'contact_info': 'Phone: 9876543222',
        'status': 'pending',
        'is_approved': True
    },
    {
        'title': 'Found Glasses Case',
        'description': 'Found a black glasses case with prescription glasses inside. Found in the lecture hall.',
        'category': 'accessories',
        'location_found': 'Lecture Hall, Building C, Room 101',
        'date_found': date.today() - timedelta(days=2),
        'contact_info': 'Phone: 9876543223',
        'status': 'pending',
        'is_approved': True
    },
    {
        'title': 'Found Mathematics Notebook',
        'description': 'Found a notebook with mathematics notes. Has name "Sarah" written on the first page.',
        'category': 'books',
        'location_found': 'Mathematics Department, 2nd Floor',
        'date_found': date.today() - timedelta(days=1),
        'contact_info': 'Email: notebook@campus.edu',
        'status': 'pending',
        'is_approved': True
    }
]

# Create Lost Items
print("\nCreating Lost Items...")
for item_data in lost_items_data:
    item, created = LostItem.objects.get_or_create(
        title=item_data['title'],
        posted_by=user,
        defaults=item_data
    )
    if created:
        print(f"  [OK] Created: {item.title}")
    else:
        # Update existing item to be approved
        item.is_approved = True
        item.status = item_data['status']
        item.save()
        print(f"  [UPDATED] Updated: {item.title}")

# Create Found Items
print("\nCreating Found Items...")
for item_data in found_items_data:
    item, created = FoundItem.objects.get_or_create(
        title=item_data['title'],
        posted_by=user,
        defaults=item_data
    )
    if created:
        print(f"  [OK] Created: {item.title}")
    else:
        # Update existing item to be approved
        item.is_approved = True
        item.status = item_data['status']
        item.save()
        print(f"  [UPDATED] Updated: {item.title}")

# Summary
print("\n" + "="*50)
print("TEST DATA SUMMARY")
print("="*50)
print(f"Total Lost Items: {LostItem.objects.filter(is_approved=True).count()}")
print(f"Total Found Items: {FoundItem.objects.filter(is_approved=True).count()}")
print(f"\nTest User: {user.username} (Password: test123)")
print("\nYou can now test the pages:")
print("  - Lost Items: http://127.0.0.1:8000/lost-items/")
print("  - Found Items: http://127.0.0.1:8000/found-items/")
print("="*50)

