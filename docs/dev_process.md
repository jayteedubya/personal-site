# Development process

## Initialization
1. With venv active, run `django-admin startproject <project_name> <project_directory>`. This will generate a new django project.
2. cd into the newly created `<project_name>` folder and and run `python manage.py runserver` to run the server and make sure everything generated correctly. NOTE: This only happens if in the settings.py file for your app `DEBUG` is set to `True`.

## Creating an app

Within Django, an app is a subsection of the overall project. Think of how you would normally set up routers in an express js application. For example, the blog app will be accessible at <your_site>/blog.

1. run `python manage.py startapp blog` to create the new app template.
2. create a file called `urls.py` in the app.
3. create a view in `views.py`
4. register the view in the `urls.py` of the app
3. register the new app in the `urls.py` of the project 

## Configuring the database

