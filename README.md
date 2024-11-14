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
