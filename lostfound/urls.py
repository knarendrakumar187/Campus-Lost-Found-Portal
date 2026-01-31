"""
URL patterns for lostfound app.
This file maps URLs to view functions.

Example:
- URL: /lost-items/ → calls lost_items_list view
- URL: /post-lost/ → calls post_lost_item view
"""

from django.urls import path
from . import views

# urlpatterns is a list of URL patterns
urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    
    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Profile
    path('profile/', views.profile, name='profile'),
    
    # Post items
    path('post-lost/', views.post_lost_item, name='post_lost'),
    path('post-found/', views.post_found_item, name='post_found'),
    
    # View items
    path('lost-items/', views.lost_items_list, name='lost_items_list'),
    path('found-items/', views.found_items_list, name='found_items_list'),
    
    # Item details
    path('lost-item/<int:pk>/', views.lost_item_detail, name='lost_item_detail'),
    path('found-item/<int:pk>/', views.found_item_detail, name='found_item_detail'),
]

