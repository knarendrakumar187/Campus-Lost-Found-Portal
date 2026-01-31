"""
Views are functions that handle web requests.
When a user visits a URL, Django calls the corresponding view function.
Views process data and return HTML pages.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import LostItem, FoundItem, UserProfile
from .forms import (
    UserRegistrationForm, UserProfileForm,
    LostItemForm, FoundItemForm
)


def home(request):
    """
    Home page view.
    Shows recent lost and found items.
    """
    # Get recent approved items (limit to 6 each)
    recent_lost = LostItem.objects.filter(is_approved=True).order_by('-created_at')[:6]
    recent_found = FoundItem.objects.filter(is_approved=True).order_by('-created_at')[:6]
    
    # Pass data to template
    context = {
        'recent_lost': recent_lost,
        'recent_found': recent_found,
    }
    return render(request, 'lostfound/home.html', context)


def register(request):
    """
    Student registration view.
    Handles both GET (show form) and POST (process form) requests.
    """
    if request.method == 'POST':
        # User submitted the form
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save()
            
            # Create user profile
            UserProfile.objects.create(user=user)
            
            # Log the user in automatically
            login(request, user)
            
            messages.success(request, 'Registration successful! Welcome!')
            return redirect('home')
    else:
        # User is just viewing the form (GET request)
        form = UserRegistrationForm()
    
    return render(request, 'lostfound/register.html', {'form': form})


def login_view(request):
    """
    Login view.
    Uses Django's built-in authentication.
    """
    if request.method == 'POST':
        from django.contrib.auth import authenticate
        
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        # Check if username and password are correct
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Login successful
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            # Login failed
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'lostfound/login.html')


def logout_view(request):
    """
    Logout view.
    """
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required
def profile(request):
    """
    User profile page.
    @login_required means: user must be logged in to access this page.
    """
    # Get or create user profile
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # Update profile
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    
    # Get user's posts
    user_lost_items = LostItem.objects.filter(posted_by=request.user)
    user_found_items = FoundItem.objects.filter(posted_by=request.user)
    
    context = {
        'profile': profile,
        'form': form,
        'user_lost_items': user_lost_items,
        'user_found_items': user_found_items,
    }
    return render(request, 'lostfound/profile.html', context)


@login_required
def post_lost_item(request):
    """
    View for posting a lost item.
    """
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
        # request.FILES contains uploaded images
        
        if form.is_valid():
            # Save the item, but don't commit to database yet
            lost_item = form.save(commit=False)
            # Set who posted it
            lost_item.posted_by = request.user
            # Save to database
            lost_item.save()
            
            messages.success(
                request,
                'Your lost item post has been submitted! It will appear after admin approval.'
            )
            return redirect('lost_items_list')
    else:
        form = LostItemForm()
    
    return render(request, 'lostfound/post_lost.html', {'form': form})


@login_required
def post_found_item(request):
    """
    View for posting a found item.
    """
    if request.method == 'POST':
        form = FoundItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            found_item = form.save(commit=False)
            found_item.posted_by = request.user
            found_item.save()
            
            messages.success(
                request,
                'Your found item post has been submitted! It will appear after admin approval.'
            )
            return redirect('found_items_list')
    else:
        form = FoundItemForm()
    
    return render(request, 'lostfound/post_found.html', {'form': form})


def lost_items_list(request):
    """
    View all lost items (approved only).
    """
    # Get search query from URL
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    
    # Start with all approved lost items
    items = LostItem.objects.filter(is_approved=True)
    
    # Filter by search query (search in title and description)
    if query:
        items = items.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        # Q objects allow complex queries
        # icontains = case-insensitive contains
    
    # Filter by category
    if category:
        items = items.filter(category=category)
    
    # Order by newest first
    items = items.order_by('-created_at')
    
    context = {
        'items': items,
        'query': query,
        'category': category,
    }
    return render(request, 'lostfound/lost_items_list.html', context)


def found_items_list(request):
    """
    View all found items (approved only).
    """
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    
    items = FoundItem.objects.filter(is_approved=True)
    
    if query:
        items = items.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    
    if category:
        items = items.filter(category=category)
    
    items = items.order_by('-created_at')
    
    context = {
        'items': items,
        'query': query,
        'category': category,
    }
    return render(request, 'lostfound/found_items_list.html', context)


def lost_item_detail(request, pk):
    """
    View details of a specific lost item.
    pk = primary key (unique ID of the item)
    """
    item = get_object_or_404(LostItem, pk=pk, is_approved=True)
    # get_object_or_404: Get the item, or show 404 error if not found
    
    context = {
        'item': item,
    }
    return render(request, 'lostfound/lost_item_detail.html', context)


def found_item_detail(request, pk):
    """
    View details of a specific found item.
    """
    item = get_object_or_404(FoundItem, pk=pk, is_approved=True)
    
    context = {
        'item': item,
    }
    return render(request, 'lostfound/found_item_detail.html', context)

@login_required
def mark_found(request, pk):
    """
    Allow user to mark their lost item as found.
    """
    item = get_object_or_404(LostItem, pk=pk)
    
    # Check if user is the owner
    if item.posted_by != request.user:
        messages.error(request, "You are not authorized to edit this item.")
        return redirect('lost_item_detail', pk=pk)
        
    if request.method == 'POST':
        item.status = 'found'
        item.save()
        messages.success(request, "Great news! Your item has been marked as found.")
        return redirect('lost_item_detail', pk=pk)
        
    return redirect('lost_item_detail', pk=pk)
