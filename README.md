# Laptop Depot

**Top Brands at Great Deals**  

At Laptop Depot, we understand that your laptop isn’t just a device—it’s your partner in productivity, creativity, and connection. That’s why we focus on offering laptops from four of the most trusted brands in the world: HP, Dell, Apple, and Lenovo. Whether you need a reliable workhorse for everyday tasks, a sleek and stylish device for presentations, or powerful performance for demanding projects, we’ve got you covered.  

Our platform is built for working professionals who value quality, efficiency, and great deals. We know that investing in the right laptop is an important decision, so we’ve made it easy for you to compare options, browse specifications, and make an informed choice that meets your unique needs.  

At Laptop Depot, we believe in keeping things simple and authentic. Our mantra, *Top Brands at Great Deals*, isn’t just a slogan—it’s the principle behind everything we do. We work to bring you competitive prices without compromising on quality or service.  

Whether you’re upgrading your current device, switching brands, or looking for a laptop that complements your work style, Laptop Depot is here to help. Explore our collection, take your pick, and let’s find the perfect laptop to power your goals.


# Set Up
Django project structure for **Laptop Depot**, designed to keep the code modular, scalable, and maintainable

---

### **1. Project Structure**

```plaintext
laptop_depot/                # Project Root
├── manage.py                # Django's management script
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (e.g., secrets, database URLs)
├── laptop_depot/            # Project configuration
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py              # WSGI entry point for deployment
│   ├── asgi.py              # ASGI entry point for async tasks
├── apps/                    # Custom apps folder
│   ├── users/               # User management app
│   │   ├── __init__.py
│   │   ├── admin.py         # Admin customization for users
│   │   ├── apps.py          # App configuration
│   │   ├── models.py        # User models (extends AbstractUser)
│   │   ├── serializers.py   # Serializers for API endpoints
│   │   ├── urls.py          # URLs specific to users
│   │   ├── views.py         # Views (e.g., register, login, profile)
│   │   ├── tests.py         # Unit tests for user functionality
│   │   ├── forms.py         # Forms (e.g., user registration)
│   │   └── templates/       # HTML templates for user-related views
│   │       └── users/
│   │           └── login.html
│   ├── products/            # Product management app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py        # Product, Brand, Category models
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests.py
│   ├── cart/                # Shopping cart app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py        # CartItem model
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests.py
│   ├── orders/              # Order management app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py        # Order, OrderItem models
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests.py
│   ├── discounts/           # Discounts and promotions app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py        # Discount model
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests.py
├── static/                  # Static files (CSS, JavaScript, images)
│   ├── css/
│   ├── js/
│   └── images/
├── media/                   # User-uploaded content (e.g., product images)
├── templates/               # Global HTML templates
│   ├── base.html            # Base template for extending
│   ├── navbar.html          # Navbar partial
│   └── footer.html          # Footer partial
├── db.sqlite3               # SQLite database (use PostgreSQL in production)
├── logs/                    # Log files for debugging
│   ├── error.log
│   ├── access.log
```

---

### **2. Detailed Explanation**

#### **Main Project (`laptop_depot`)**
- **`settings.py`**:
  - Configure apps, middleware, database, and static/media file handling.
  - Load secrets and environment variables from `.env` (use `django-environ`).
- **`urls.py`**:
  - Route global URLs and include app-specific routes.
- **`wsgi.py`/`asgi.py`**:
  - Deployment entry points for WSGI or ASGI servers.

#### **Custom Apps (`apps/`)**
- Create each app for a specific functionality (e.g., `users`, `products`, `cart`) to ensure separation of concerns.
- Each app includes its own `models.py`, `views.py`, `urls.py`, and `serializers.py`.

#### **Static and Media**
- **Static Files**: For frontend assets like CSS, JS, and images.
- **Media Files**: For user-uploaded content like product images or profile pictures.

#### **Templates**
- Use a global `base.html` to define a consistent structure for your site (e.g., header, footer, navbar).
- Organize app-specific templates in their respective app directories.

#### **Testing**
- Include unit tests for models, views, and APIs in each app’s `tests.py`.

---

### **3. Steps to Set Up**

1. **Initialize the Project**
   ```bash
   django-admin startproject laptop_depot .
   ```

2. **Create Custom Apps**
   ```bash
   python manage.py startapp users
   python manage.py startapp products
   python manage.py startapp cart
   python manage.py startapp orders
   python manage.py startapp discounts
   ```

3. **Install Dependencies**
   - Add necessary libraries to `requirements.txt`, e.g.:
     ```plaintext
     django
     djangorestframework
     django-environ
     pillow  # For image handling
     django-cors-headers  # For frontend-backend communication
     ```

4. **Set Up Database**
   - Use PostgreSQL for production and configure it in `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'laptop_depot',
             'USER': 'username',
             'PASSWORD': 'password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Configure Static and Media Files**
   ```python
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [BASE_DIR / 'static']
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'
   ```

6. **Run Initial Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---

