
# Sample Boilerplate for Django Rest Framework

## Overview
Django Rest Framework Project Setup Sample for Interns

### Dependencies
 - Dependencies are managed inside the requirement folder.
 - Better use  [Poetry](https://python-poetry.org/) package

To manage dependencies, we recommend using [Poetry](https://python-poetry.org/) for Python package management:

1. **Install Poetry:**
   ```bash
   curl -sSL https://install.python-poetry.org | python -
   ```

2. **Initialize Project with Poetry:**
   ```bash
   poetry init
   ```

3. **Add Dependencies to `pyproject.toml`:**
   ```toml
   [tool.poetry.dependencies]
   python = "^3.9"
   django = "^3.2.7"
   djangorestframework = "^3.12.4"
   ```

4. **Install Dependencies:**
   ```bash
   poetry install
   ```

### Running Local Development Server

1. **Set Up Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

2. **Install Packages and Dependencies:**
   ```bash
   pip install -r requirements/dev.txt
   ```

3. **Environment Variables:**
   - Copy `sample.env.py` to `env.py` and configure necessary environment variables like database credentials, API keys, etc.

4. **Initialize Database:**
   ```bash
   python manage.py migrate
   ```

5. **Run Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Development Server:**
   - Open your web browser and go to `http://127.0.0.1:8000/` to see the Django project running.

### Project Structure

```
boilerplate-drf/
│
├── config/                    # Configuration files
│   ├── __init__.py
│   ├── settings.py                # Base settings
│   └── urls.py                # Main URL configuration
│
├── apps/                      # Django apps directory
│   ├── app1/                  # Example app 1
│   │   ├── api/
│   │   │   └── v1/            # API version 1
│   │   │       ├── __init__.py
│   │   │       ├── serializers.py  # Serializers for API v1
│   │   │       ├── urls.py         # URL configuration for API v1
│   │   │       └── views.py        # Views (API endpoints) for API v1
│   │   ├── migrations/         # Database migrations for app1
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py           # Models for app1
│   │   ├── tests/              # Unit tests for app1
│   │   │   ├── __init__.py
│   │   │   └── test_views.py
│   │   ├── urls.py             # Main URL configuration for app1 (include API URLs here if needed)
│   │   └── views.py            # Views (non-API endpoints) for app1
│   └── ...                     # Other apps can be structured similarly
│
│
├── requirements/              # Requirements files
│   ├── base.txt               # Base dependencies
│   └── dev.txt                # Development dependencies
│
├── sample.env.py/             # Sample environment variables template
│   
├── env.py                     # Environment variables (not committed)
│
└── README.md                  # Project documentation

```

### Additional Resources

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django Rest Framework Documentation](https://www.django-rest-framework.org/)
- [Poetry Documentation](https://python-poetry.org/docs/)
