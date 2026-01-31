# Campus Lost & Found Portal - Complete Django Tutorial

Welcome! This is a complete step-by-step guide to building a Campus Lost & Found Portal using Django. I'll explain everything in simple language, assuming you're a beginner.

---

## 📋 Table of Contents

1. [Project Overview](#step-1-project-overview)
2. [Technology Setup](#step-2-technology-setup)
3. [Create Django Project & App](#step-3-create-django-project--app)
4. [Database Design](#step-4-database-design)
5. [User Authentication](#step-5-user-authentication)
6. [Core Functionalities](#step-6-core-functionalities)
7. [Admin Panel](#step-7-admin-panel)
8. [Frontend](#step-8-frontend)
9. [Testing](#step-9-testing)
10. [Deployment](#step-10-deployment)

---

## Step 1: Project Overview

### What Problem Does This Portal Solve?

**Problem:** Students lose items on campus (phones, wallets, books, etc.) and have no easy way to:
- Report lost items
- Report found items
- Search for their lost items
- Contact people who found their items

**Solution:** A web portal where:
- Students can post about lost items
- Students can post about found items
- Everyone can search and browse items
- Contact information is shared securely
- Admin can approve posts to prevent spam

### Who Will Use It?

1. **Students** (Regular Users):
   - Register and login
   - Post lost/found items
   - Search and browse items
   - Contact other students

2. **Admin** (Campus Staff):
   - Login to admin panel
   - Approve/reject posts
   - Mark items as returned
   - Remove fake posts

### Main Features

✅ User registration and login  
✅ Post lost items with images  
✅ Post found items with images  
✅ View all lost/found items  
✅ Search by keyword and category  
✅ Contact person feature  
✅ Admin approval system  
✅ User profile management  

---

## Step 2: Technology Setup

### Python Version
- **Recommended:** Python 3.8 or higher
- Check your version: `python --version` or `python3 --version`

### Django Version
- **Using:** Django 4.2.7 (stable and beginner-friendly)
- This version works well with Python 3.8+

### Virtual Environment Setup

**Why use a virtual environment?**
- Keeps your project dependencies separate
- Prevents conflicts with other Python projects
- Makes deployment easier

**Commands to create virtual environment:**

**On Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# You should see (venv) in your terminal
```

**On Mac/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# You should see (venv) in your terminal
```

**To deactivate later:**
```bash
deactivate
```

### Required Packages

The project includes a `requirements.txt` file with:
- `Django==4.2.7` - The web framework
- `Pillow==10.1.0` - For handling images

**Install packages:**
```bash
pip install -r requirements.txt
```

### Project Folder Structure

```
campus_portal/          # Main project folder
├── campus_portal/      # Project settings
│   ├── __init__.py
│   ├── settings.py     # All configuration
│   ├── urls.py         # Main URL routing
│   ├── wsgi.py         # For deployment
│   └── asgi.py         # For async deployment
├── lostfound/          # Our app (the main functionality)
│   ├── migrations/     # Database changes
│   ├── __init__.py
│   ├── admin.py        # Admin panel config
│   ├── apps.py
│   ├── models.py       # Database models
│   ├── views.py        # Request handlers
│   ├── urls.py         # App URL routing
│   └── forms.py        # Form definitions
├── templates/          # HTML templates
│   └── lostfound/
│       ├── base.html
│       ├── home.html
│       └── ...
├── static/             # CSS, JS, images
│   └── css/
│       └── style.css
├── media/              # User uploaded files (created automatically)
├── db.sqlite3          # Database file (created automatically)
├── manage.py           # Django management script
├── requirements.txt    # Dependencies
└── README.md          # This file
```

---

## Step 3: Create Django Project & App

### Understanding Django Structure

**Project vs App:**
- **Project:** The entire website (campus_portal)
- **App:** A feature/module (lostfound)

One project can have multiple apps (e.g., lostfound, blog, forum).

### Commands to Create Project

**Note:** The project structure is already created for you! But here's what happened:

```bash
# Create Django project
django-admin startproject campus_portal

# Navigate into project
cd campus_portal

# Create app
python manage.py startapp lostfound
```

### Settings.py Changes Explained

**Key settings in `campus_portal/settings.py`:**

1. **INSTALLED_APPS:** List of all apps Django should use
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       # ... other apps
       'lostfound',  # Our app!
   ]
   ```

2. **DATABASES:** Which database to use
   - SQLite (default) - Perfect for beginners, file-based
   - No setup needed!

3. **TEMPLATES:** Where to find HTML files
   ```python
   'DIRS': [BASE_DIR / 'templates'],
   ```

4. **STATIC_URL & MEDIA_URL:** For CSS/images and user uploads
   ```python
   STATIC_URL = 'static/'
   MEDIA_URL = 'media/'
   ```

5. **LOGIN_URL:** Where to redirect if user not logged in
   ```python
   LOGIN_URL = 'login'
   ```

---

## Step 4: Database Design

### What are Models?

**Models = Database Tables**

Think of a model as a blueprint:
- **Model class** = Table name
- **Model attributes** = Column names
- **Model instance** = One row in the table

### Our Models Explained

#### 1. UserProfile Model

**Purpose:** Store extra information about students (phone, student ID)

**Fields:**
- `user` - Links to Django's built-in User (username, email, password)
- `phone` - Student's phone number (optional)
- `student_id` - Student ID number (optional)
- `created_at` - When profile was created (automatic)

**Why needed?** Django's User model has basic info. We add campus-specific info here.

#### 2. LostItem Model

**Purpose:** Store information about lost items

**Fields:**
- `posted_by` - Who posted it (links to User)
- `title` - Short title (e.g., "Lost iPhone 12")
- `description` - Detailed description
- `category` - Type of item (electronics, clothing, etc.)
- `location_lost` - Where it was lost
- `date_lost` - When it was lost
- `image` - Photo of the item (optional)
- `contact_info` - How to contact the person
- `status` - Current status (pending, found, returned)
- `is_approved` - Admin approval flag (prevents spam)
- `created_at` - When post was created
- `updated_at` - When post was last updated

**Why these fields?**
- Title/Description: Help people identify the item
- Category: Makes searching easier
- Location/Date: Important clues
- Image: Visual confirmation
- Contact: How to reach the owner
- Status: Track if item is still lost
- is_approved: Admin can filter spam

#### 3. FoundItem Model

**Purpose:** Store information about found items

**Similar structure to LostItem**, but with:
- `location_found` instead of `location_lost`
- `date_found` instead of `date_lost`

### Database Relationships Explained

1. **OneToOneField (User ↔ UserProfile):**
   - One User = One Profile
   - Like: One person = One passport

2. **ForeignKey (User → LostItem):**
   - One User can have Many LostItems
   - Like: One student can post many lost items

### Creating Database Tables

**After defining models, create tables:**

```bash
# Create migration files (records changes to models)
python manage.py makemigrations

# Apply migrations (create actual database tables)
python manage.py migrate
```

**What happens:**
1. `makemigrations` creates Python files describing database changes
2. `migrate` executes those changes, creating tables in SQLite

---

## Step 5: User Authentication

### How Authentication Works

1. **Registration:** User creates account → stored in database
2. **Login:** User enters credentials → Django checks database → creates session
3. **Logout:** Session destroyed → user logged out

### Registration Flow

**File: `lostfound/views.py` - `register()` function**

```python
def register(request):
    if request.method == 'POST':
        # User submitted form
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create user
            UserProfile.objects.create(user=user)  # Create profile
            login(request, user)  # Auto-login
            return redirect('home')
    else:
        # Show form
        form = UserRegistrationForm()
    return render(request, 'lostfound/register.html', {'form': form})
```

**What happens:**
1. User visits `/register/`
2. Sees registration form
3. Fills form and submits
4. Django validates data
5. Creates User and UserProfile
6. Logs user in automatically
7. Redirects to home page

### Login Flow

**File: `lostfound/views.py` - `login_view()` function**

```python
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'lostfound/login.html')
```

**What happens:**
1. User enters username/password
2. Django checks if credentials match
3. If yes: Create session, redirect to home
4. If no: Show error message

### Role-Based Access

**How to protect pages:**

```python
@login_required  # Decorator = must be logged in
def post_lost_item(request):
    # Only logged-in users can access this
    ...
```

**In templates:**
```html
{% if user.is_authenticated %}
    <!-- Show this to logged-in users -->
    <a href="{% url 'post_lost' %}">Post Lost Item</a>
{% else %}
    <!-- Show this to guests -->
    <a href="{% url 'login' %}">Login</a>
{% endif %}
```

**Admin vs Regular User:**
- Django's User model has `is_staff` flag
- Admin panel only accessible if `is_staff=True`
- We'll create admin user later

---

## Step 6: Core Functionalities

### 1. Post a Lost Item

**File: `lostfound/views.py` - `post_lost_item()`**

**Flow:**
1. User clicks "Post Lost"
2. Sees form (title, description, category, etc.)
3. Fills form and uploads image (optional)
4. Submits form
5. Item saved with `is_approved=False`
6. Admin must approve before it appears publicly

**Key code:**
```python
lost_item = form.save(commit=False)  # Don't save yet
lost_item.posted_by = request.user    # Set the owner
lost_item.save()                      # Now save
```

### 2. Post a Found Item

**Similar to lost items**, but uses `FoundItem` model.

### 3. View All Lost Items

**File: `lostfound/views.py` - `lost_items_list()`**

**Features:**
- Shows only approved items (`is_approved=True`)
- Ordered by newest first
- Supports search and category filter

**Search implementation:**
```python
query = request.GET.get('q', '')  # Get search term from URL
if query:
    items = items.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    # Search in title OR description (case-insensitive)
```

### 4. View All Found Items

**Same as lost items**, but for found items.

### 5. Search Items

**How it works:**
1. User enters keyword in search box
2. Selects category (optional)
3. Clicks "Search"
4. URL becomes: `/lost-items/?q=iphone&category=electronics`
5. View filters database based on query
6. Shows matching results

**Q Objects Explained:**
```python
Q(title__icontains=query) | Q(description__icontains=query)
```
- `Q()` = Complex query object
- `icontains` = Case-insensitive "contains"
- `|` = OR operator
- Searches in title OR description

### 6. Contact Person Feature

**How it works:**
- Each post has `contact_info` field
- Displayed on item detail page
- Users can see phone/email and contact directly
- No built-in messaging (keeps it simple)

**In template:**
```html
<div class="contact-section">
    <h3>Contact Information</h3>
    <p>{{ item.contact_info }}</p>
</div>
```

---

## Step 7: Admin Panel

### What is Admin Panel?

Django's built-in admin interface for managing data. No need to write custom admin pages!

### Setting Up Admin

**1. Create admin user:**
```bash
python manage.py createsuperuser
```
- Enter username, email, password
- This user can access `/admin/`

**2. Register models in `lostfound/admin.py`:**

Already done! Models are registered with:
- List display (what columns to show)
- Filters (easy filtering)
- Search (search functionality)
- Editable fields (quick edit)

### Admin Features

**1. Approve Posts:**
- Admin sees all posts (approved and pending)
- Can check/uncheck `is_approved` checkbox
- Only approved posts appear on public pages

**2. Mark as Returned:**
- Admin can change status to "returned"
- Helps track which items are resolved

**3. Remove Fake Posts:**
- Admin can delete posts
- Or uncheck `is_approved` to hide them

**4. View User Information:**
- See all registered users
- View user profiles
- Can edit user data if needed

---

## Step 8: Frontend

### Template Structure

**Base Template (`base.html`):**
- Contains navigation bar
- Footer
- Message display area
- Other pages extend this

**Template Inheritance:**
```html
{% extends 'lostfound/base.html' %}
{% block content %}
    <!-- Page-specific content -->
{% endblock %}
```

### Forms

**Django Forms handle:**
- HTML generation
- Validation
- Error display
- Data cleaning

**Example in template:**
```html
<form method="post">
    {% csrf_token %}  <!-- Security token -->
    {{ form.title }}   <!-- Renders input field -->
    {{ form.description }}
    <button type="submit">Submit</button>
</form>
```

### Basic CSS

**File: `static/css/style.css`**

**Key styles:**
- Navigation bar (dark blue)
- Cards for items (white with shadow)
- Forms (clean, modern)
- Buttons (blue primary, gray secondary)
- Responsive design (works on mobile)

**No complex design** - Simple, clean, functional!

### Messages & Alerts

**Django messages framework:**
```python
messages.success(request, 'Item posted successfully!')
messages.error(request, 'Something went wrong!')
messages.info(request, 'Please login to continue.')
```

**Display in template:**
```html
{% if messages %}
    {% for message in messages %}
        <div class="alert alert-{{ message.tags }}">
            {{ message }}
        </div>
    {% endfor %}
{% endif %}
```

**Message types:**
- `success` - Green (good news)
- `error` - Red (problems)
- `info` - Blue (information)

---

## Step 9: Testing

### Running the Server

**Start development server:**
```bash
python manage.py runserver
```

**Access:**
- Website: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

### Sample Test Data

**1. Create admin user:**
```bash
python manage.py createsuperuser
# Username: admin
# Email: admin@campus.edu
# Password: admin123 (or your choice)
```

**2. Create test student:**
- Go to http://127.0.0.1:8000/register/
- Register as: `student1`, password: `test123`
- Login and post a lost item

**3. Approve posts:**
- Login to admin panel
- Go to "Lost items"
- Check `is_approved` for test post
- Now it appears on public pages

### Common Errors and Fixes

**1. "No module named 'django'"**
- **Fix:** Activate virtual environment, then `pip install -r requirements.txt`

**2. "TemplateDoesNotExist"**
- **Fix:** Check `settings.py` - `TEMPLATES['DIRS']` should include `BASE_DIR / 'templates'`

**3. "Static files not loading"**
- **Fix:** Check `settings.py` - `STATICFILES_DIRS` should include `BASE_DIR / 'static'`
- Run: `python manage.py collectstatic` (for production)

**4. "Image upload not working"**
- **Fix:** Check `MEDIA_ROOT` and `MEDIA_URL` in settings
- Make sure `enctype="multipart/form-data"` in form tag

**5. "CSRF verification failed"**
- **Fix:** Make sure `{% csrf_token %}` is in all forms
- Check `MIDDLEWARE` includes `CsrfViewMiddleware`

**6. "Database errors"**
- **Fix:** Run migrations: `python manage.py makemigrations` then `python manage.py migrate`

**7. "Page not found (404)"**
- **Fix:** Check URL patterns in `urls.py`
- Make sure app URLs are included in main `urls.py`

---

## Step 10: Deployment

### Running on Local Server

**Already done!** Just run:
```bash
python manage.py runserver
```

**Access at:** http://127.0.0.1:8000/

### Prepare for Production Deployment

**1. Change SECRET_KEY:**
```python
# In settings.py
SECRET_KEY = 'your-random-secret-key-here'
# Generate one: https://djecrety.ir/
```

**2. Set DEBUG = False:**
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

**3. Collect static files:**
```bash
python manage.py collectstatic
```

**4. Set up proper database:**
- SQLite is fine for small sites
- For production, use PostgreSQL or MySQL

**5. Use environment variables:**
```python
import os
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
```

### Deployment Options

**Free options:**
- **PythonAnywhere** - Easy for beginners
- **Heroku** - Popular, free tier available
- **Railway** - Modern, easy setup

**Steps for PythonAnywhere:**
1. Create account
2. Upload project files
3. Install dependencies
4. Run migrations
5. Configure web app
6. Done!

---

## 🚀 Quick Start Guide

**For beginners - get it running in 5 minutes:**

```bash
# 1. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create database tables
python manage.py makemigrations
python manage.py migrate

# 4. Create admin user
python manage.py createsuperuser

# 5. Run server
python manage.py runserver

# 6. Open browser
# Go to: http://127.0.0.1:8000/
```

---

## 📚 Key Concepts Explained

### MVC Pattern (Django uses MVT)

- **Model (M):** Database structure (`models.py`)
- **View (V):** Request handlers (`views.py`)
- **Template (T):** HTML files (`templates/`)

**Flow:**
1. User visits URL
2. Django finds view function
3. View gets data from Model
4. View passes data to Template
5. Template renders HTML
6. HTML sent to user

### URL Routing

**How URLs work:**
```
URL: /lost-items/
     ↓
urls.py finds pattern
     ↓
Calls view function: lost_items_list()
     ↓
View returns HTML
```

### Forms in Django

**Two types:**
1. **Regular forms** - For simple data
2. **Model forms** - Tied to models (auto-generate fields)

**Our forms are ModelForms:**
- Automatically match model fields
- Handle validation
- Save to database easily

---

## 🎓 Learning Resources

**Django Official Docs:**
- https://docs.djangoproject.com/

**Django Tutorial:**
- https://docs.djangoproject.com/en/4.2/intro/tutorial01/

**Python Basics:**
- https://www.python.org/about/gettingstarted/



