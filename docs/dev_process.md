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
1. settings.py in the `<project_name>` folder is where you configure your database settings, timezone, installed apps, etc
2. because there are some default apps installed (things to handle sessions, admin, auth, etc) we need to do an initial database migration to set up their required tables. do this by running `python manage.py migrate`. You will also do this whenever you update models in your own apps.
3. At the core of database usage in Django is the model. these are created in the `models.py` file of your app.
4. Now that we have a model, we need to add our app to `INSTALLED_APPS` in settings.py. you'll want to use python import syntax from the outermost folder of the project (i.e. for the blog use `"blog.apps.BlogConfig"`)
5. once the app is registered, we will need to build the migrations again. use the `python manage.py makemigrations <app_name>` command. You can view the SQL for these migrations in `<app_name>/migrations`.
6. now that the migrations have been generated, run them with `python manage.py migrate`
7. You can use `python manage.py shell` to open an interactive shell to access the database and insert test values or other tasks like that.


## Admin
1. create an administrator account using `python manage.py createsuperuser` (NOTE: in local environment username is admin and password is guest, yes this is stupid but it's for local dev only)
2. in `<app_name>/admin.py`, register the the app using `admin.site.register(<app>)`
3. run `python manage.py runserver` then go to 127.0.0.1/admin/ and you will see the sign in prompt. you can now make modifications to the apps.


## Creating Views
1. in the `views.py` file in the root of your app, add a function that returns an `HttpResponse` object
2. register the function in the app level `urls.py`
3. create a folder called templates in the root of the app, then within that folder create another folder with the name of the app.
This is necessary because Django will match the first template that matches the path project wide, meaning the wrong template could be loaded
