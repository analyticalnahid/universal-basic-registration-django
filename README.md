# universal-basic-registration-django

## 1.Install django-crispy-forms:
pip install django-crispy-forms

## 2.Set up django-crispy-forms in your Django project:
    - Install the package: pip install django-crispy-forms
    - Add 'crispy_forms' to the INSTALLED_APPS list in your Django settings.py file.
    - Specify the template pack to use by adding the following line to your settings.py: CRISPY_TEMPLATE_PACK = 'bootstrap4'
    - Load the crispy forms in your template by adding this line in your template: {% load crispy_forms_tags %}
    
    Examples:-
    
    INSTALLED_APPS = [
    ...
    'app_login'
    'crispy_forms',
    ...
    ]

    CRISPY_TEMPLATE_PACK = 'bootstrap4'
