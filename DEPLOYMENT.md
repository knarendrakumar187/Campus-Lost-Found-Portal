# Deploy to Get a Live Preview Link

If you want a **public URL** that anyone can access, you need to deploy the project. Here are free options:

## Option 1: PythonAnywhere (Easiest for Beginners) ⭐

### Steps:
1. **Sign up:** https://www.pythonanywhere.com/ (Free account available)
2. **Upload files:**
   - Go to "Files" tab
   - Upload your project folder
3. **Set up web app:**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose Django, select your project
4. **Configure:**
   - Set source code path
   - Set WSGI file path: `campus_portal/wsgi.py`
5. **Run migrations:**
   - Open Bash console
   - Run: `python manage.py migrate`
6. **Create superuser:**
   - Run: `python manage.py createsuperuser`
7. **Reload web app**

**Result:** You'll get a URL like: `https://yourusername.pythonanywhere.com`

---

## Option 2: Railway (Modern & Easy)

### Steps:
1. **Sign up:** https://railway.app/ (Free tier available)
2. **Connect GitHub:**
   - Push your code to GitHub
   - Connect Railway to your repo
3. **Auto-deploy:**
   - Railway detects Django
   - Automatically sets up
4. **Add environment variables:**
   - `SECRET_KEY` (generate a new one)
   - `DEBUG=False`
   - `ALLOWED_HOSTS=your-app.railway.app`
5. **Run migrations:**
   - Use Railway's console or add to startup

**Result:** You'll get a URL like: `https://your-app.railway.app`

---

## Option 3: Render (Simple & Free)

### Steps:
1. **Sign up:** https://render.com/ (Free tier available)
2. **Create Web Service:**
   - Connect GitHub repo
   - Choose "Web Service"
   - Build command: `pip install -r requirements.txt`
   - Start command: `python manage.py migrate && python create_superuser.py && gunicorn campus_portal.wsgi:application`
3. **Add environment variables:**
   - `SECRET_KEY`
   - `DEBUG=False`
   - `ALLOWED_HOSTS=your-app.onrender.com`
4. **Deploy**

**Result:** You'll get a URL like: `https://your-app.onrender.com`

---

## Option 4: Heroku (Popular but requires credit card)

### Steps:
1. **Install Heroku CLI:** https://devcenter.heroku.com/articles/heroku-cli
2. **Login:**
   ```bash
   heroku login
   ```
3. **Create app:**
   ```bash
   heroku create your-app-name
   ```
4. **Set environment variables:**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app.herokuapp.com
   ```
5. **Deploy:**
   ```bash
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

**Result:** You'll get a URL like: `https://your-app.herokuapp.com`

---

## Before Deploying - Update Settings

**Important:** Update `campus_portal/settings.py`:

```python
# Change these for production:
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']

# Add these for static files:
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

**Generate a new SECRET_KEY:**
- Visit: https://djecrety.ir/
- Copy the generated key
- Use it as environment variable

---

## Quick Comparison

| Platform | Free Tier | Ease | Best For |
|----------|-----------|------|----------|
| PythonAnywhere | ✅ Yes | ⭐⭐⭐⭐⭐ | Beginners |
| Railway | ✅ Yes | ⭐⭐⭐⭐ | Modern apps |
| Render | ✅ Yes | ⭐⭐⭐⭐ | Simple deployment |
| Heroku | ⚠️ Requires card | ⭐⭐⭐ | Popular choice |

---

## Recommended: PythonAnywhere for Beginners

**Why?**
- Easiest setup
- No command line needed (web interface)
- Free tier available
- Perfect for learning

**Time to deploy:** ~15 minutes

---

## Need Help?

1. **PythonAnywhere Tutorial:** https://help.pythonanywhere.com/pages/DeployExistingDjangoProject
2. **Railway Docs:** https://docs.railway.app/
3. **Render Docs:** https://render.com/docs

---

**Once deployed, you'll have a live preview link! 🚀**

