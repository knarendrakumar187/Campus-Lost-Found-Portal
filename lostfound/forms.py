"""
Forms are used to collect data from users.
Django forms handle validation, HTML generation, and data cleaning.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import LostItem, FoundItem, UserProfile


class UserRegistrationForm(UserCreationForm):
    """
    Form for student registration.
    Extends Django's built-in UserCreationForm.
    """
    email = forms.EmailField(required=True)
    # Email field with validation
    
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    
    class Meta:
        # Meta class tells Django which model and fields to use
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        # password1 and password2 are for password confirmation
    
    def __init__(self, *args, **kwargs):
        # Customize form appearance
        super().__init__(*args, **kwargs)
        # Add CSS classes to make forms look better
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile (phone, student_id).
    """
    class Meta:
        model = UserProfile
        fields = ['phone', 'student_id']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., +1234567890'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., STU12345'}),
        }


class LostItemForm(forms.ModelForm):
    """
    Form for posting a lost item.
    """
    class Meta:
        model = LostItem
        fields = ['title', 'description', 'category', 'location_lost', 'date_lost', 'image', 'contact_info']
        # Fields that users can fill
        
        widgets = {
            # Customize how each field looks
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Lost iPhone 12 Pro'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe your lost item in detail...'
            }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'location_lost': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Library, 2nd floor, Room 205'
            }),
            'date_lost': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'  # HTML5 date picker
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'  # Only accept images
            }),
            'contact_info': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your phone number or email'
            }),
        }


class FoundItemForm(forms.ModelForm):
    """
    Form for posting a found item.
    """
    class Meta:
        model = FoundItem
        fields = ['title', 'description', 'category', 'location_found', 'date_found', 'image', 'contact_info']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Found Black Wallet'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe the found item...'
            }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'location_found': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Cafeteria, near entrance'
            }),
            'date_found': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'contact_info': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your phone number or email'
            }),
        }

