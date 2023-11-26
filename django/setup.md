create a folder where your projects will be hosted
install django in a virtual environment using the code below
```terminal
pipenv install django
```
after installation, it will create a virtual environment, copy the file path to the environment and cd into it.
or use the code below to see the path
```terminal
pipenv --venv
```
then copy the path written and cd into it

to start a basic project in django, you could use the command
```terminal 
django-admin startproject project_name .
```
where the dot it necessary if you dont want django to create an extra directory to the directory that contains the files
if you wish to run django project on vscode using the virtual environment, copy the path that was generated, search for python intepreter.
select the path config and paste the path with /bin/python at the end

to run the django,
```terminal
python manage.py runserver
```
in django, there are apps created which is default within the program for instance auth, session etc, however, we can create our app as well using the startapp function. To do this, we run the command
```terminal
python manage.py startapp newAppName
```
after the above, it create some files, first migrations used for templating, and others each for a certain purpose
After creating the new app, we need to register the new app in the settings module. to do this, simple open the setting app in the precious main folder (storefront) and write the name of the file in the list of apps, for this case we will write playground

## Views
A view function is a function that takes a request and returns a response just like the https sending a request and have a response. its basically called request handler. 
now lets create our first view object
```python
from django.shortcuts import render

from django.http import HttpResponse

  

# Create your views here.

def hello(request):

    return HttpResponse("Hello World")
```
	after the above, we need to map the url to the view function 
To do this, we define a urls.py file. you can name it anything but by convention, its best to name it using urls for easy comprehension. 
in the file, call the django.urls to link your urls.py file to the view function

After the above, declare a variable name, call it urlpatterns.
Note: this name is strict just like using template in flask as the django will use that name for its search

After the above, we need to reference the url we just create to the main urls
within the main urls, there's a comment that tell us how to add new urls, simply follow the instructions given 
```instructions
Including another URLconf

    1. Import the include() function: from django.urls import include, path

    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
```
the python code will become
```python
"""

URL configuration for storefront project.

  

The `urlpatterns` list routes URLs to views. For more information please see:

    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Examples:

Function views

    1. Add an import:  from my_app import views

    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views

    1. Add an import:  from other_app.views import Home

    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf

    1. Import the include() function: from django.urls import include, path

    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.contrib import admin

from django.urls import path, include

  

urlpatterns = [

    path('admin/', admin.site.urls),

    path('playground/', include('playground.urls'))

]
```

## Templates
templates are use to hold html files just like flask, lets create a template folder with an index.html file. 
To do this, we use the html render option and pass in the request parameter into the function and return the html file to be rendered.
```python
from django.shortcuts import render

from django.http import HttpResponse

  

# Create your views here.

def hello(request):

    return render(request, "index.html")
```

```html
<h1> Hello World </h1>
```

we could also use jinja templating with django to render a dynamic content by adding a third argument to the view function we defined above
e.g
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):

    return render(request, "index.html", {"name": "Gentle"})
```

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    {% if name %}

        <h1>Hello {{ name }}</h1>

    {% else %}

        <h1>Hello World</h1>

    {% endif %}

</body>

</html>
```

## Debug django
to debug in django, we could use the break point or use the django debug toolbar. using the command 
```terminal
pipenv install django debug-toolbar

```
after this, add the debug-toolbar to the list of applications in your django settings

the below link give full guide on django debug tool and how to configure it
```link
[Installation — Django Debug Toolbar 4.2.0 documentation (django-debug-toolbar.readthedocs.io)](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
```
[Installation — Django Debug Toolbar 4.2.0 documentation (django-debug-toolbar.readthedocs.io)](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
In the link above, the step 4 to 6 are necessary to lunch the debug mode in django_debugger, others could be overlooked for now

## Data Model
