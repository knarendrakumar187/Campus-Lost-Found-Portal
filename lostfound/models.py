"""
Models are like blueprints for your database tables.
Each model class = one database table
Each attribute = one column in the table

Think of models as the structure of your data.
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    """
    Extended user information for students.
    Django's built-in User model has: username, email, password
    We add: phone, student_id, etc.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # OneToOneField means: One User = One UserProfile (like a passport)
    
    phone = models.CharField(max_length=15, blank=True)
    # CharField = text field, max_length = maximum characters allowed
    # blank=True means this field is optional
    
    student_id = models.CharField(max_length=20, blank=True)
    # Student ID number
    
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True means: automatically set when object is created
    
    def __str__(self):
        # This makes the object readable when printed
        return f"{self.user.username}'s Profile"


class LostItem(models.Model):
    """
    Model for items that students have lost.
    Each lost item = one row in the database table.
    """
    
    # Category choices - dropdown options
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('books', 'Books'),
        ('accessories', 'Accessories'),
        ('documents', 'Documents'),
        ('other', 'Other'),
    ]
    
    # Status choices
    STATUS_CHOICES = [
        ('pending', 'Still Looking'),
        ('found', 'Found'),
        ('returned', 'Returned'),
    ]
    
    # Who posted this item
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # ForeignKey = many-to-one relationship
    # Many LostItems can belong to one User
    # on_delete=models.CASCADE means: if user is deleted, delete their posts too
    
    title = models.CharField(max_length=200)
    # Title of the lost item (e.g., "Lost iPhone 12")
    
    description = models.TextField()
    # TextField = longer text (unlimited length)
    # Description of the item
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    # Category with predefined choices
    
    location_lost = models.CharField(max_length=200)
    # Where the item was lost (e.g., "Library, 2nd floor")
    
    date_lost = models.DateField()
    # When the item was lost
    
    image = models.ImageField(upload_to='lost_items/', blank=True, null=True)
    # Image of the item
    # upload_to='lost_items/' means: save images in media/lost_items/ folder
    # blank=True, null=True means: image is optional
    
    contact_info = models.CharField(max_length=200)
    # How to contact the person (phone, email, etc.)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    # Current status of the item
    
    is_approved = models.BooleanField(default=False)
    # Admin must approve posts before they appear (prevents spam)
    
    created_at = models.DateTimeField(auto_now_add=True)
    # When the post was created
    
    updated_at = models.DateTimeField(auto_now=True)
    # auto_now=True means: automatically update when object is modified
    
    def __str__(self):
        return f"{self.title} - {self.posted_by.username}"


class FoundItem(models.Model):
    """
    Model for items that students have found.
    Similar structure to LostItem.
    """
    
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('books', 'Books'),
        ('accessories', 'Accessories'),
        ('documents', 'Documents'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Waiting for Claim'),
        ('claimed', 'Claimed'),
        ('returned', 'Returned to Owner'),
    ]
    
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # Who found the item
    
    title = models.CharField(max_length=200)
    # Title (e.g., "Found Black Wallet")
    
    description = models.TextField()
    # Description of found item
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    
    location_found = models.CharField(max_length=200)
    # Where the item was found
    
    date_found = models.DateField()
    # When the item was found
    
    image = models.ImageField(upload_to='found_items/', blank=True, null=True)
    # Image of the found item
    
    contact_info = models.CharField(max_length=200)
    # How to contact the finder
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    is_approved = models.BooleanField(default=False)
    # Admin approval required
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.posted_by.username}"

