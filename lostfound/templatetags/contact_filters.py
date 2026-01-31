"""
Custom template filters for making contact information clickable
"""
import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def make_contact_clickable(text):
    """
    Converts plain text contact information into clickable links.
    Detects emails and phone numbers and makes them clickable.
    """
    if not text:
        return text
    
    # Pattern for email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Pattern for phone numbers (various formats)
    phone_pattern = r'(\+?\d{1,3}[-.\s]?)?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}'
    
    result = text
    
    # Replace emails with mailto links
    def replace_email(match):
        email = match.group(0)
        return f'<a href="mailto:{email}" class="contact-link email-link">📧 {email}</a>'
    
    result = re.sub(email_pattern, replace_email, result)
    
    # Replace phone numbers with tel links
    def replace_phone(match):
        phone = match.group(0).strip()
        # Clean phone number for tel: link (remove spaces, dashes, etc.)
        clean_phone = re.sub(r'[^\d+]', '', phone)
        return f'<a href="tel:{clean_phone}" class="contact-link phone-link">📞 {phone}</a>'
    
    result = re.sub(phone_pattern, replace_phone, result)
    
    return mark_safe(result)

