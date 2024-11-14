# Django Project Setup Guide

This guide will walk you through setting up a Django development environment, including necessary tools, configurations, and the creation of a custom user model.

## Prerequisites

1.  **Python** - Install the latest version of Python if not already installed.
2.  **Virtualenv** - For creating an isolated environment.
3.  **PostgreSQL** - Used as the database for the Django application.

## Installation Steps

### Step 1: Set Up the Project Directory

1.  **Create a new directory** for your Django project:

```bash
mkdir django-project
cd django-project
```

2. Create a virtual environment:

```bash
python -m virtualenv venv
```

3. Activate the virtual environment:

- On Windows

```bash
.\venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

## Step 2: Install Django and Required Packages

1. Install Django:

```bash
pip install Django
```

2. Install psycopg2-binary for PostgreSQL connection:

```bash
pip install psycopg2-binary
```

3. Install python-dotenv to manage environment variables:

```bash
pip install python-dotenv
```

## Step 3: Set Up Django Project and Apps

1. Create a new Django project:

```bash
django-admin startproject core
```

2. Navigate to the project folder:

```bash
cd core
```

3. Create applications:

- `home` app

```bash
python manage.py startapp home
```

- `custom_admin` app

```bash
python manage.py startapp custom_admin
```

4. Run the development server to ensure the setup is working:

```bash
python manage.py runserver
```

## Step 4: Configure PostgreSQL Database

1.  Create a PostgreSQL database\*\* named `django_db`.
2.  Configure environment variables\*\* in a `.env` file:
    - Add `.env` file in the root of your project and add the following:

```env
DB_NAME=django_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

3. Update Django settings to use the .env variables:
   - Open core/settings.py and add the following at the top:

```python
import os
from pathlib import Path
from dotenv import load_dotenv

# env setup
load_dotenv()

# Update the `DATABASES` configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

## Step 5: Create Custom User Model

1. Define the custom user model in home/models.py:

```bash
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    role = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
```

2. Specify the custom user model in `core/settings.py`:

```bash
AUTH_USER_MODEL = 'home.User'
```

3. Create and apply migrations for the custom user model:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 6: Set Up Base HTML Template

1. Create a base HTML template named `_base.html`
   \*\*Place the file in `templates/_base.html`

```html
{% load compress %} {% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Django + Tailwind CSS + Flowbite</title>

    {% compress css %}
    <link rel="stylesheet" href="{% static 'src/output.css' %}" />
    {% endcompress %}
  </head>

  <body class="bg-green-50">
    <div class="container mx-auto mt-4">
      {% block content %} {% endblock content %}
    </div>
  </body>
</html>
```

## Additional Setup Notes

- Static files: Ensure static files are properly configured for styles and scripts.
- Testing: Run `python manage.py runserver` and navigate to `http://127.0.0.1:8000` to verify the setup.
