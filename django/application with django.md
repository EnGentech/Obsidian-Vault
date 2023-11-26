install the django 
confirm the installation by checking the version 
```terminal
python -m django --version
```

lets create an environment to work with
follow the following to install the environment
```terminal
sudo apt install python3.10-env

python3 -m venv environment_name

source environment_name/bin/active

# to deactivate simple type deactivate
```

After the installation, django has a file called admin which describes all the basic applications we could run with django. to view these files, we use the command
```django
django-admin
```
To start a new project, we use the startproject app on the django admin, this will create all the necessary files for us to get started with django project.
```terminal
django-admin startproject project_name
```


## Application and route
lets create our first app called blog
```terminal
python manage.py startapp blog
```

first we create a function for rendering but for now lets use HttpRequest
```python
from django.shortcuts import render

from django.http import HttpRequest
 

# Create your views here.

def home(request):

    """return a home page"""

    return HttpRequest("<h1>Blog Home page</h1>")
```

after the above, we will create a new urls.py file to store our url with the content 
```python
from django.urls import path

from . import views

  

urlpatterns = [

    path('', views.home, name="blog-home"),

]
```

in the view.py
```python
from django.shortcuts import render

from django.http import HttpResponse

  

# Create your views here.

def home(request):

    """return a home page"""

    return HttpResponse("<h1>Blog Home page</h1>")
```
then in the main urls.py
```python
from django.contrib import admin

from django.urls import path, include

  

urlpatterns = [

    path('admin/', admin.site.urls),

    path("blog/", include("blog.urls"))

]
```

furthermore, you will notice that each time you try to visit the localhost route, there will be a 404 error because the landing url is not mapped to any urls, to do that remove the value int the project urls e.g
```python
path("", include("blog.urls"))
```
this will return the localhost page as the home page

## Templates
create a folder inside the templates known as blog but this is not necessary. however creating that will need a few more settings
go to the app.py in the blog and copy the class name. proceed to the settings and add the app to the app list to look like
```python
  

INSTALLED_APPS = [

    'blog.app.BlogConfig',

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

]

```
to render the page, we do the following
```python
def home(request):

    """return a home page"""

    return render(request, "blog/home.html")
```

## Using Jinja
lets use jinja for a loop variable called post which is send from django. this is the same thing in flask. first we create a domy post values in a list of dictionaries
```python
from django.shortcuts import render

from django.http import HttpResponse

from datetime import datetime

  

posts = [{

    'author': "Gentle Inyang",

    'date': datetime.now(),

    'content': "This is my first post on the webpage"

},

{

    'author': "Blessing Emmanuel",

    'date': datetime.now(),

    'content': "This is another post on my webpage"

}

]

  

# Create your views here.

def home(request):

    """return a home page"""

    return render(request, "blog/home.html", {'posts': posts})

  

def about_us(request):

    """return about_us page"""

    return HttpResponse("<h3>About Us page</h3>")
```
then in the html file, we have 

```html
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>

</head>

<body>

    <h2>This are the latest post on my blog!</h2>

    {% for post in posts %}

        <h3>Post created by: {{ post.author }}</h3>

        <h5>Posted on: {{ post.date }}</h5>

        <h5>message: {{ post.content }}</h5>

    {% endfor %}

</body>

</html>
```

## Loading css in django
In flask we use url_for(), but in django, we will use the jinja syntax. first create a folder in the root of your directory called static, this is where django will look for css, images and other files like js. create all your files within this file location. on calling it, follow the below code in the inherited file.
```html
{% load static %}

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="{% static 'blog/main.css' %}">

    <title>Document</title>

</head>

<body>

    <h2>This are the latest post on my blog!</h2>

    {% for post in posts %}

        <h3>Post created by: {{ post.author }}</h3>

        <h5>Posted on: {{ post.date }}</h5>

        <h5>message: {{ post.content }}</h5>

    {% endfor %}

</body>

</html>
```

## Setting up Django admin page
First we will have to create a super user which will be used to access the admin page of django
to do this, we will first set our user ORM table by running the code below on the console
```terminal
python manage.py migrate

python manage.py createmigrations

python manage.py createsuperuser

```
After the above, you will be prompted to enter a username, email and password. do the above and validate you password. now run the runserver option and log into the admin

## Database table creation
One important thing about django in terms of creating database is that you can change you database without having to change your codes, for instance you can use sqllite, sqldb or even postgress using the same code in your django. 
All that is needed is for you to setup the database you wish to use and reuse the codes you had.
The database in django is represented by class.

We are going to create just two tables for illustration, the user table and the post table, however, django have created a user model for us and for now we will levarage on that for our user table.
to create a database, open up the model.py app and input he following

The class we will create will inherit from the model class which is an inbuilt
```python
from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

  

# Create your models here.

# inherit from the model class

"""

Each class in here is a table in database while its

attribute is the fields in the table when created

"""

class Post(models.Model):

    title = models.CharField(max_length=100, null=False)

    # the CharFields is similar to the TextField only for the difference

    # that its an unrestricted field containing lines and lines of texts

    content = models.TextField()

    '''date_posted = models.DateField(auto_now_add=True), this option is good'''

    # when the date will not be updated but for this case, we may update the date

    # if theres changes to the title of the content hence not the appropriate way

    # hence the best approach is to set the datetime field to default parameter

    date_posted = models.DateField(default=timezone.now)

    # this is creating a one to many relationshiop

    author = models.ForeignKey(User, on_delete=models.CASCADE)
```
After the above, re-run makemigrations to effect changes

If properly done, django will create a file in migration folder with a class name Migration have a file name called 001...
This will also automatically generate an ID which will be set to the primary key for the table created

The file in here will be created once the migrate command is executed in the database

If you want to see the sql representation of what we have executed, you will need to get the migration file path created by django using only the folder name and the file number after creation and run the below code
```terminal
python manage.py sqlmigrate file_path

# example
python manage.py sqlmigrate blog 0001
```
Now lets run the migrate command to enact the changes into our database
```terminal
python manage.py migrate
```

## Query database with shell
Having run this, lets query the database using the shell terminal, the django shell provides a terminal similar to the python shell, we could run python commands in there and could also run django commands as well
```terminal
python manage.py shell

# the above will pop the shell CLI
```

lets do basic CRUD operation
to query the database
```terminal
User.objects.all()
# running the above returns all users that have been created

# if there was more than one user, you can use .first() to get the first user
# last method to get the last method
```

## Query by filter
```terminal
User.objects.filter(username="EnGentech")

# to get the first user if there was more that one match filter, 

User.objects.filter(username="EnGentech").first()
```

## Getting the properties of the filtered result
```terminal
user = User.objects.filter(username="EnGentech").first()
user.pk    or    user.id

# the above will return the id of the user that was created by django
```

Instead of using the filter, we could also use the .get method which works pretty well like the filter
```terminal
user = User.objects.first(id=1)
```

## Creating a POST
for now the post is empty if we are to query to post table, so lets create a post
```terminal
post_1 = Post(title="Django training", content="I have a class to present today", author=user)

```
from the above, if we query the database, we will have nothing to populated in there because we have not save it to the database, to save, we use the command
```terminal
post_1.save()

```
after this re-run the query and we should have the post populated to the database

We can use the foreign key information to get the details of the user as well. for example:
```terminal
post = Post.objects.filter(author=1).first()
post.author.email
```
this will return the email that was registered by the user

## Basic way to get all post by user
In as much as we can query the database to get all the post
```terminal
user.post_set

# however, this will return some bunch of code 
```
hence we can do this

```terminal
user.post_set.all()  # to view all post from the user
user.post_set.create(title='new title' ...) # to create new post of the user

# the beauty of this one is that you dont need to pass your author since the post_set captures the active user and you dont need to run .save() as it automatically save this to the database
```

since we have learn this basic, lets head to our domy data that we used to populate our website and make some changes by using a dynamic data in there

to format the time rendered on the webpage, you can you the django builtin formatting found on its docs here
link: [Built-in template tags and filters | Django documentation | Django (djangoproject.com)](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/)
not this is done in the jinja file like
{{ post.date_posted | date: "F, d, Y"}}

## Admin register
Now if we go to the admin page for our django, the POST table wont be there, we need to register that unto django admin for it to be rendered, hence to do that simply open the admin.py file, import the table class you wish to register and write a simple line of code as seen below 

```python
from django.contrib import admin

from blog.models import Post

  

# Register your models here.

admin.site.register(Post)
```