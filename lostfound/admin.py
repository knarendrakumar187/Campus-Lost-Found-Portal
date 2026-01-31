"""
Admin panel configuration.
This file controls what appears in Django's admin interface.
Admin can approve posts, mark items as returned, etc.
"""

from django.contrib import admin
from .models import UserProfile, LostItem, FoundItem


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Configure how UserProfile appears in admin panel.
    """
    list_display = ['user', 'student_id', 'phone', 'created_at']
    # What columns to show in the list view
    search_fields = ['user__username', 'student_id']
    # Allow searching by username and student_id


@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    """
    Configure LostItem admin interface.
    """
    list_display = ['title', 'posted_by', 'category', 'status', 'is_approved', 'created_at']
    # Columns to display
    
    list_filter = ['category', 'status', 'is_approved', 'created_at']
    # Filters on the right side (for easy filtering)
    
    search_fields = ['title', 'description', 'posted_by__username']
    # Search functionality
    
    list_editable = ['is_approved', 'status']
    # Allow editing directly from list view (quick approve/reject)
    
    readonly_fields = ['created_at', 'updated_at']
    # These fields can't be edited (auto-generated)


@admin.register(FoundItem)
class FoundItemAdmin(admin.ModelAdmin):
    """
    Configure FoundItem admin interface.
    """
    list_display = ['title', 'posted_by', 'category', 'status', 'is_approved', 'created_at']
    list_filter = ['category', 'status', 'is_approved', 'created_at']
    search_fields = ['title', 'description', 'posted_by__username']
    list_editable = ['is_approved', 'status']
    readonly_fields = ['created_at', 'updated_at']

