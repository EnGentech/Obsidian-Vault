This sheet will guide us on creating a full web application to takes in username and password from users, upload profile pictures and as well change password if forgotten, its going to be a long view but exercise and follow up. theres light at the end of the tunnel. If u feel the introduction is quite simple, feel free to skip.

First install flask and other dependencies in associate
```terminal
pip install flask
```
to confirm if flask has been installed successfully, run python terminal and import flask, if theres no error, then the journey is yours. 
Note that for you to follow up on this article, you need to have basic knowledge of python and the web and a bit of database
```python
python
>>> import flask
>>> 
```
if after the above, you have no error message, then your installation was successful. Congratulations

Lets proceed

To keep things simple, create a directory that will take all your files together. In this article, we create a directory named Flask_blog with our first .py file as [Quickstart — Flask Documentation (2.3.x) (palletsprojects.com)](https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application)
Now its time to commence our transit to creating our blog with flask

Coming from the simplest application, visit the flask documentation website on flask.pocoo.org.
In this session, I'll copy and paste the first simple code as seen on the page
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

the first line is the importation of flask
the second is is a variable (app) declared to instantiate the flask class while the __name__ is a special variable in python which is used by flask to determine where to find your template and static files.

A route is simply what we type in the browser to navigate where and what page should be displayed on the web page. There are lots of behind the seen in the route but you dont need to worry about that as that has been handled. the "/" is the home page of our web page and the function to be returned when running flask is followed. 

To run the flask, there are two ways, first is to create a virtual environment at where flask will run from or you run it programmatically. 
to run it via virtual environment, we call
```linux and apple
export FLASK_APP=filename
```
```windows
set FLASK_APP=filename
```
after the environment is set, we can run our application by simply running 
```any_os
flask run
```

Meanwhile if the above does not run, you will need to invoke the environment variable in windows using the below code before the flask run
```python
$env:FLASK_APP = 'file_name'
```

on running the code, you will notice an IP address pop up to the terminal, copy that IP and paste on your url, the message defined on the function defined should be seen on the web page, to further make things easy, replace the IP with localhost with the port number 5000.
```url
localhost:5000
```

We can also use html tags to run the code for instance instead of running return "Hello World!", run it message to be displayed with tags
```python
return "<h1>Hello World!</h1>"
```
rerun the server and reload the page, boom, that should work
Now: its gonna be difficult to rerun the server each time you make changes to your code hence its needful to create a means by which your webserver should be automatically updated at each moment of making changes to the code, to do this, we run the server in a debug mode
```linux
export FLASK_DEGUG=1
or use set instead of export for windows OS
```
With this, each time you make changes to your code, you dont need to re-run your web server instead you only reload your web page and thats cool

However, if you dont want to run your code in the environment variable, you can do that within the python code  as seen below
```python
from flask import Flask  
  
app = Flask(__name__)  
  
@app.route("/", strict_slashes=False)  
def home():  
return "<h1>Hello World! from me</h1>"  
  
if __name__ == "__main__":  
app.run(debug=True)
```

Having done the above, now lets add about_page to our code as a route to give us certain information as we dim fit.
```python
from flask import Flask  
  
app = Flask(__name__)  
  
@app.route("/", strict_slashes=False)  
def home():  
return "<h1>Hello World! from me</h1>"  
  
@app.route("/about", strict_slashes=False)  
def about():  
return "<h1>About page</h1>"  
  
if __name__ == "__main__":  
app.run(debug=True)
```
to see the content of the about, we change our url to include a file path just as seen below
```url
localhost:5000/about
```
We can define two routes to mean same thing, for instance, if we need to create our home page to reflect the default url, then we can create two route within the same function just like this
```python
from flask import Flask  
  
app = Flask(__name__)  
  
@app.route("/home")  
@app.route("/", strict_slashes=False)  
def home():  
return "<h1>Hello World! from me</h1>"  
  
@app.route("/about", strict_slashes=False)  
def about():  
return "<h1>About page</h1>"  
  
if __name__ == "__main__":  
app.run(debug=True)
```
In the above  case
```url
localhost:5000
localhost:5000/home
```
the above url will return the same web content since they are both pointing to the same function definition

## Template
This part will address templating our webpages and adding variables to the web page. 
What are templates?
Imagine that we have multiple routes that need to be written using html codes like the example below
```python
from flask import Flask  
  
app = Flask(__name__)  
  
@app.route("/home")  
@app.route("/", strict_slashes=False)  
def home():  
return """  
<!doctype html>  
<html>  
<head>  
<title>Home_page</title>  
</head>  
<body>  
<h1>Head content</h1>  
<p>This is the head content of the home page</p>  
</body>  
</html>  
"""  
  
@app.route("/about", strict_slashes=False)  
def about():  
return "<h1>About page</h1>"  
  
if __name__ == "__main__":  
app.run(debug=True)
```
Looking at the above code, we used html code to render the page, lets assume that we had more content to write for about up to 10 routes, then the code page may be extremely large, another thing here is that the code may be repeated. 
To resolve this we need a template. flask mostly looks for files in template directory otherwise the directory must be specified, for this article we will create a directory named templates and write our code in there.
```terminal
mkdir templates
```
Lets create two files, one for home page and the other for about page
```terminal
cd templates
touch home.html
touch about.html
```

Inside the home.html, create a basic html file with Home Page just like this. but note that we will not be covering most of html code, that is covered in another article except the concepts that includes flask
```html
<!doctype html>  
<html lang="en">  
<head>  
<meta charset="UTF-8">  
<meta name="viewport"  
content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">  
<meta http-equiv="X-UA-Compatible" content="ie=edge">  
<title>Document</title>  
</head>  
<body>  
<h1>Home Page</h1>  
</body>  
</html>
```
We can now render the file through flask application by importing render_template from flask class just like below
```python 
from flask import Flask, render_template  
  
app = Flask(__name__)  
  
@app.route("/home")  
@app.route("/", strict_slashes=False)  
def home():  
return render_template("home.html")  
  
@app.route("/about", strict_slashes=False)  
def about():  
return "<h1>About page</h1>"  
  
if __name__ == "__main__":  
app.run(debug=True)
```
so instead of writing the entire file in here, we can write them in different html files and render them as seen above. We can do same for the about page and make changes where necessary.
What we have created above is a simple static web page, but in present days, web pages are more of being dynamic rather than static, the creates the flexibility of post, get, delete and put. 
We will advance our code a little bit to create a little bit of dynamism in our code 
Lets create a post list and populate it in our web page
```python 
# creating the post list
from flask import Flask, render_template  
  
app = Flask(__name__)  
  
posts = [  
{  
'author': "Gentle Inyang",  
'title': 'blog post 1',  
'content': 'First post content',  
'date posted': '28 July 2022'  
},  
{  
'author': "EnGentech services",  
'title': 'blog post 2',  
'content': 'Second post content',  
'date posted': '20 July 2022'  
}  
]  
  
@app.route("/home")  
@app.route("/", strict_slashes=False)  
def home():  
return render_template("home.html", post=posts) # a variable name that will be used to populate the content of the list in the webpage  
  
@app.route("/about", strict_slashes=False)  
def about():  
return "<h1>About page</h1>"  
  
if __name__ == "__main__":  
app.run(debug=True)
```
To populate the above in the web page, we will edit our html code with jinja codes which is used by flask to interact between the backend and the frontend
```html
<!doctype html>  
<html lang="en">  
<head>  
<meta charset="UTF-8">  
<meta name="viewport"  
content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">  
<meta http-equiv="X-UA-Compatible" content="ie=edge">  
<title>Document</title>  
</head>  
<body>  
<h1>Home Page</h1>  
{% for pt in post %}  
<h3> {{ pt.title }}</h3>  
<p>by {{ pt.author }} on {{ pt.date_created }}</p>  
<p>{{ pt.content }}</p>  
{% endfor %}  
</body>  
</html>
```
The above will loop through and create the details as seen on the page. if the page is view with view source code, we will notice that the we page will generate all the values that has been loop through in a full html code context rather than the jinja code written above.
Lets make our title dynamic such that if theres is title in the page, the title should be printed alongside the flag blog as default title

We will repeat the same in the about page and pass title=About in the render_template, but there's a naïve code in here, that's the codes we have here is repeating, this implies that if we need to make a change which will affect all of our code, then the code needs to be changed per route. This is not a good practice. hence to handle that we will create a base code called layout.html and then pass the code into other routes. This layout will be used to write codes that is expected to be repeated across other routes. To accomplish this, the template inheritance is used

```html
<!doctype html>  
<html lang="en">  
<head>  
<meta charset="UTF-8">  
<meta name="viewport"  
content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">  
<meta http-equiv="X-UA-Compatible" content="ie=edge">  
{% if title %}  
<title>Flag Post - {{ title }}</title>  
{% else %}  
<title>Flag Post</title>  
{% endif %}  
</head>  
<body>  
  
</body>  
</html>
```
Inside the layout, we will create a blog,
A blog is simply a parent blog that can be inherited and changes can be made by the child.
we add the blog into the body tag thus:
```html
<body>  
{% block content %}{% endblock %}  
</body>
```
Now we will remove every other codes from the previous defined files and inherit the file properties from the layout.html
```html
<!--home page -->
{% extends "layout.html" %}  
{% block content %}  
<h1>Home Page</h1>  
{% for pt in post %}  
<h3> {{ pt.title }}</h3>  
<p>by {{ pt.author }} on {{ pt.date_created }}</p>  
<p>{{ pt.content }}</p>  
{% endfor %}  
{% endblock content %}
```
In the above, the endblock content is not actually necessary as endblock is enough to handle the task, however, I input the content to enhance clarity on which block was open and was closed. DO THE SAME THING FOR THE ABOUT PAGE

We can see how powerful this has been, in addition if you have a style to be used across all your webpages either from bootstrap or coded by you, this powerful tool allows you to create a one time layout to be used across multiple pages, lets use bootstrap to illustrate this.
```html
<!doctype html>  
<html lang="en">  
<head>  
<meta charset="UTF-8">  
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">  
<meta name="viewport"  
content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">  
<meta http-equiv="X-UA-Compatible" content="ie=edge">  
{% if title %}  
<title>Flag Post - {{ title }}</title>  
{% else %}  
<title>Flag Post</title>  
{% endif %}  
</head>  
<body>  
<div class="container">  
{% block content %}{% endblock %}  
</div>  
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>  
</body>  
</html>
```
adding the js and css link defines a bootstrap compatibility into our code and the class='container' defined above is a bootstrap class that enhances the settings of the webpage created by adjusting the margins and padding of elements within the class. Run the code and see the changes.

Lets add more functionality to the code by creating  a nav bar and other stuffs
```html
<!doctype html>  
<html lang="en">  
<head>  
<meta charset="UTF-8">  
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">  
<meta name="viewport"  
content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">  
<meta http-equiv="X-UA-Compatible" content="ie=edge">  
{% if title %}  
<title>Flag Post - {{ title }}</title>  
{% else %}  
<title>Flag Post</title>  
{% endif %}  
</head>  
<body>  
<header class="site-header">  
<nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">  
<div class="container">  
<a class="navbar-brand mr-4" href="/">Flask Blog</a>  
<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">  
<span class="navbar-toggler-icon"></span>  
</button>  
<div class="collapse navbar-collapse" id="navbarToggle">  
<div class="navbar-nav mr-auto">  
<a class="nav-item nav-link" href="/">Home</a>  
<a class="nav-item nav-link" href="/about">About</a>  
</div>  
<!-- Navbar Right Side -->  
<div class="navbar-nav">  
<a class="nav-item nav-link" href="/login">Login</a>  
<a class="nav-item nav-link" href="/register">Register</a>  
</div>  
</div>  
</div>  
</nav>  
</header>  
<main role="main" class="container">  
<div class="row">  
<div class="col-md-8">  
{% block content %}{% endblock %}  
</div>  
<div class="col-md-4">  
<div class="content-section">  
<h3>Our Sidebar</h3>  
<p class='text-muted'>You can put any information here you'd like.  
<ul class="list-group">  
<li class="list-group-item list-group-item-light">Latest Posts</li>  
<li class="list-group-item list-group-item-light">Announcements</li>  
<li class="list-group-item list-group-item-light">Calendars</li>  
<li class="list-group-item list-group-item-light">etc</li>  
</ul>  
</p>  
</div>  
</div>  
</div>  
</main>  
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>  
</body>  
</html>
```

We will hence create our css and js files but this has to be in a directory called static which is the default directory that flask reads for such files
create a file name main.css
```css
body {  
background: #fafafa;  
color: #333333;  
margin-top: 5rem;  
}  
  
h1, h2, h3, h4, h5, h6 {  
color: #444444;  
}  
  
.bg-steel {  
background-color: #5f788a;  
}  
  
.site-header .navbar-nav .nav-link {  
color: #cbd5db;  
}  
  
.site-header .navbar-nav .nav-link:hover {  
color: #ffffff;  
}  
  
.site-header .navbar-nav .nav-link.active {  
font-weight: 500;  
}  
  
.content-section {  
background: #ffffff;  
padding: 10px 20px;  
border: 1px solid #dddddd;  
border-radius: 3px;  
margin-bottom: 20px;  
}  
  
.article-title {  
color: #444444;  
}  
  
a.article-title:hover {  
color: #428bca;  
text-decoration: none;  
}  
  
.article-content {  
white-space: pre-line;  
}  
  
.article-img {  
height: 65px;  
width: 65px;  
margin-right: 16px;  
}  
  
.article-metadata {  
padding-bottom: 1px;  
margin-bottom: 4px;  
border-bottom: 1px solid #e3e3e3  
}  
  
.article-metadata a:hover {  
color: #333;  
text-decoration: none;  
}  
  
.article-svg {  
width: 25px;  
height: 25px;  
vertical-align: middle;  
}  
  
.account-img {  
height: 125px;  
width: 125px;  
margin-right: 20px;  
margin-bottom: 16px;  
}  
  
.account-heading {  
font-size: 2.5rem;  
}
```
To include the above style into our flask, we will need the url_for which is a function that will find the exact location of route within the background.
First we add a css link in to our layout.html
```html
<link rel="stylesheet" type='text/css' href="{{ url_for('static', filename='main.css') }}">
```
and import url_for into our python script.

In the home page, we can modify our code to have some styles on the webpage
```html
{% extends "layout.html" %}  
{% block content %}  
<h1>Home Page</h1>  
{% for post in post %}  
<article class="media content-section">  
<div class="media-body">  
<div class="article-metadata">  
<a class="mr-2" href="#">{{ post.author }}</a>  
<small class="text-muted">{{ post.date_posted }}</small>  
</div>  
<h2><a class="article-title" href="#">{{ post.title }}</a></h2>  
<p class="article-content">{{ post.content }}</p>  
</div>  
</article>  
{% endfor %}  
{% endblock content %}
```

## Forms and Validating Input
This application will have the ability for users to create an account, login, logout, make post, delete post etc
In this part of the article, we will create a registration page where a user should signup and later sign in. Apparently we are going to do some stuffs in this session like creating a code to check for validation of some context, using regular expressions to validate user password and others. However, this may look cumbersome but its simple to implement it, however there are provision made out there for this codes to be utilized, in this article we are going to use. 
The most popular extension we can use to work with forms in flask is called WTforms, we will need to install this 
```terminal
pip install flask-wtf
```
After the installation, we can now create another file to handle the forms. 
In this case we create the form.py
Note that that the form can still be created from the exiting file but its best practice to separate all files to handle different things hence to easy modification when need arises
first import the flask_wtf
```python
from flask_wtf import FlaskForm
```
the above will enable us to create a form using python classes which will then be converted within the program into an html code

We need to define a class with the name of our expected form. in this case, we will love to build a registrationform class, hence our class will be named after the expected name 
```python
rom flask_wtf import FlaskForm  
  
class RegistrationForm(FlaskForm):
# The class in this case inherits from the FlaskForm
```
Next, we will need to define the fields of our form, and for this purpose we will need to create a username field which will take strings as input, hence the field we will create is a StringField field, we will import another module to handle this
```python
from flask_wtf import FlaskForm  
from wtforms import StringField  
  
class RegistrationForm(FlaskForm):  
username = StringField('Username')
```
The above creates a field name Username which is equivalent to label in html, however we can create some validations within our page such that users could be limited to input, for instance we can limit the input character to span between 2 to 50, the field cant be left empty and things of that nature. 
Our new code becomes 
```python 
from flask_wtf import FlaskForm  
from wtforms import StringField, PasswordField, SubmitField  
from wtforms.validators import DataRequired, Length, Email, EqualTo  
  
class RegistrationForm(FlaskForm):  
username = StringField('Username',  
validators=[DataRequired(), Length(min=2, max=20)])  
email = StringField('Email', validators=[DataRequired(), Email()])  
password = PasswordField('Password', validators=[DataRequired()])  
confirm_password = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])  
submit = SubmitField('Sign_Up')
```
In the above code, the wtforms is used to import fields that is associated to the fields we create just like the html input element, remember that in html we have inputs like password, text, submit etc.
The wtforms.validators is used to validate the expected values of our form. We will do same for the login. 

Note, for the email_validator, additional installation needs to be performed. run
```terminal
pip install email_validator
```

```python 
from flask_wtf import FlaskForm  
from wtforms import StringField, PasswordField, SubmitField, BooleanField  
from wtforms.validators import DataRequired, Length, Email, EqualTo  
  
class RegistrationForm(FlaskForm):  
username = StringField('Username',  
validators=[DataRequired(), Length(min=2, max=20)])  
email = StringField('Email', validators=[DataRequired(), Email()])  
password = PasswordField('Password', validators=[DataRequired()])  
confirm_password = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])  
submit = SubmitField('Sign_Up')  
  
class LofinForm(FlaskForm):  
email = StringField('Email', validators=[DataRequired(), Email()])  
password = PasswordField('Password', validators=[DataRequired()])  
remember = BooleanField('Remember Me')  
submit = SubmitField('Sign In')
```
In the login page, the email will be used as our login in addition to the password, the remember filed is created to save login details for next session using cookies. 

ONE more thing, we need to create a secret key for our application. the secret key is used to protect cookies modification and forgeries. to do this, we head to our main flask file, in this case flaskblock.py
```python
from flask import Flask, render_template, url_for  
  
app = Flask(__name__)  
  
app.secret_key = ''
```
The secret key is simple a list of random values generated, you can choose to generate any random characters of your choice or you use the python module that handles that, for this article, we will use the python library that handles that:
first switch to terminal and run python env
Generate the secret key using the command 
```python
>>> import secrets
>>> secrets.token_hex(24)
# Note the 24 is just the number of bytes, you can pass any number of your desire and same length will be generated, copy and paste the code to the '' above
```
```python
from flask import Flask, render_template, url_for  
  
app = Flask(__name__)  
  
app.secret_key = 'e8f62ae662f9b5677fcb601ca848590801982d9a2b33adda'
```
now lets import our registrationForm and LoginForm into our engine and create a route for it
```python 
from flask import Flask, render_template, url_for  
from form import RegistrationForm, LoginForm  
  
app = Flask(__name__)  
  
app.secret_key['SECRET_KEY'] = 'e8f62ae662f9b5677fcb601ca848590801982d9a2b33adda'
```
The full code with the route becomes 
```python
from flask import Flask, render_template, url_for  
from form import RegistrationForm, LoginForm  
  
app = Flask(__name__)  
  
app.secret_key = 'e8f62ae662f9b5677fcb601ca848590801982d9a2b33adda'  
  
posts = [  
{  
'author': "Gentle Inyang",  
'title': 'blog post 1',  
'content': 'First post content',  
'date_posted': '28 July 2022'  
},  
{  
'author': "EnGentech services",  
'title': 'blog post 2',  
'content': 'Second post content',  
'date_posted': '20 July 2022'  
}  
]  
  
@app.route("/home")  
@app.route("/", strict_slashes=False)  
def home():  
return render_template("home.html", post=posts)  
  
@app.route("/about", strict_slashes=False)  
def about():  
return render_template("about.html", title="About")  
  
@app.route("/register", strict_slashes=False)  
def register():  
form = RegistrationForm()  
return render_template("register.html", title="register", form=form)  
  
@app.route("/login", strict_slashes=False)  
def login():  
form = LoginForm()  
return render_template("login.html", title="Login", form=form)  
  
  
if __name__ == "__main__":  
app.run(debug=True)
```

Notice that we have not created the template for login in register yet, the next code will show that
Lets do that in the template directory
for the register.html template, we have the code below
```html
{% extends "layout.html" %}  
{% block content %}  
<div class="content-section">  
<form action="" method="POST">  
{{ form.hidden_tag() }}  
<fieldset class="form-group"> <!--this is a bootstrap class -->  
<legend class="border-bottom mb-4">Join Today</legend>  
<!-- the mb-4 is simply a margin bottom of 4 -->  
<div class="form-group">  
{{ form.username.label(class='form-control-label') }}  
<!-- the form.username if gotten from the form.py we created  
and will be represented as label in the html -->  
{{ form.username(class='form-control form-control-lg') }}  
</div>  
<div class="form-group">  
{{ form.email.label(class='form-control-label') }}  
{{ form.email(class='form-control form-control-lg') }}  
</div>  
<div class="form-group">  
{{ form.password.label(class='form-control-label') }}  
{{ form.password(class='form-control form-control-lg') }}  
</div>  
<div class="form-group">  
{{ form.confirm_password.label(class='form-control-label') }}  
{{ form.confirm_password(class='form-control form-control-lg') }}  
</div>  
<div class="form-group">  
{{ form.submit(class='btn btn-outline-info') }}  
</div>  
</fieldset>  
</form>  
</div>  
{% endblock content %}
```
All the above is simply calling the fields we created in our form.py and the classes there-in are all bootstrap classes which offcourse could be build from scratch if you mind doing such. 

From the above, will still need to inform users to go and sign in if they have an account already, to this this we add another div block 
```html
<div class="border-top pt-3">  
<small class="text=muted">  
Already Have An Account? <a class="ml-2" href="{{ url_for('login') }}">Sign In</a>  
<!-- note that the login is not the route login but the function name on the  
route login. Take note of this -->  
</small>  
</div>
```
If we load the web page, fill in the form and submit, we will get a message of Method not allowed because in our route we didnt create a means to collect a post method, however the best idea in this is to submit our data into a database
Basically to resolve this, we could add the methods parameter to get a POST and GET request, we will simply edit our register route with
```python
@app.route("/register", strict_slashes=False, methods=['GET', 'POST'])  
def register():  
form = RegistrationForm()  
return render_template("register.html", title="register", form=form)
```
If we submit this, we should notice that the error is no more there but one more thing, we need to validate if the form has been successfully submitted
```python
@app.route("/register", strict_slashes=False, methods=['GET', 'POST'])  
def register():  
form = RegistrationForm()  
if form.validate_on_submit():  
flash(f'Account created for {form.username.data}!', 'success')  
return render_template("register.html", title="register", form=form)
# note import flash for the flash message
```

After the above, we need to redirect a user to the home page rather than remaining on the same page after which the form is submitted. 
```python
@app.route("/register", strict_slashes=False, methods=['GET', 'POST'])  
def register():  
form = RegistrationForm()  
if form.validate_on_submit():  
flash(f'Account created for {form.username.data}!', 'success')  
return redirect(url_for('home'))  
return render_template("register.html", title="register", form=form)
```
Next we need to update our template to indicate where we will need our flash messages to display, basically the top of the page is ideal
```html
<main role="main" class="container">  
<div class="row">  
<div class="col-md-8">  
{% with messages = get_flashed_messages(with_categories=True) %}  
{% if messages %}  
{% for categories, message in messages %}  
<div class="alert alert-{{ category }}">  
{{ message }}  
</div>  
{% endfor %}  
{% endif %}  
{% endwith %}  
{% block content %}{% endblock %}  
</div>
```
In the above, we use the function get_flashed_message to get the messages populated using flash from the backend and then display it on the web page, the with categories=True is used to add the success field which was defined in the back-end. 
The condition checked if there exist any message, then if will print the message using an alert which is a means of printing and instant message on the screen using html.

On the web browser, if we fill in the correct information and hit submit, it will redirect us to the home page, however, if the input provided is not correct, for instance the email entered is not a valid mail address, the program will return us back to the same page but the user needs to know the error. lets handle this 
On the registration form, we updated the content thus:
```html
{% extends "layout.html" %}  
{% block content %}  
<div class="content-section">  
<form action="" method="POST">  
{{ form.hidden_tag() }}  
<fieldset class="form-group"> <!--this is a bootstrap class -->  
<legend class="border-bottom mb-4">Join Today</legend>  
<!-- the mb-4 is simply a margin bottom of 4 -->  
<div class="form-group">  
{{ form.username.label(class='form-control-label') }}  
<!-- the form.username if gotten from the form.py we created  
and will be represented as label in the html -->  
{% if form.username.errors %}  
{{ form.username(class='form-control form-control-lg is-invalid') }}  
<div class="invalid-feedback">  
{% for error in form.username.errors %}  
<span>{{ error }}</span>  
{% endfor %}  
</div>  
{% else %}  
{{ form.username(class='form-control form-control-lg') }}  
{% endif %}  
</div>  
<div class="form-group">  
{{ form.email.label(class='form-control-label') }}  
  
{% if form.email.errors %}  
{{ form.email(class='form-control form-control-lg is-invalid') }}  
<div class="invalid-feedback">  
{% for error in form.email.errors %}  
<span>{{ error }}</span>  
{% endfor %}  
</div>  
{% else %}  
{{ form.email(class='form-control form-control-lg') }}  
{% endif %}  
  
</div>  
<div class="form-group">  
{{ form.password.label(class='form-control-label') }}  
{% if form.password.errors %}  
{{ form.password(class='form-control form-control-lg is-invalid') }}  
<div class="invalid-feedback">  
{% for error in form.password.errors %}  
<span>{{ error }}</span>  
{% endfor %}  
</div>  
{% else %}  
{{ form.password(class='form-control form-control-lg') }}  
{% endif %}  
</div>  
<div class="form-group">  
{{ form.confirm_password.label(class='form-control-label') }}  
{% if form.confirm_password.errors %}  
{{ form.confirm_password(class='form-control form-control-lg is-invalid') }}  
<div class="invalid-feedback">  
{% for error in form.confirm_password.errors %}  
<span>{{ error }}</span>  
{% endfor %}  
</div>  
{% else %}  
{{ form.confirm_password(class='form-control form-control-lg') }}  
{% endif %}  
</div>  
<div class="form-group">  
{{ form.submit(class='btn btn-outline-info') }}  
</div>  
</fieldset>  
</form>  
</div>  
<div class="border-top pt-3">  
<small class="text=muted">  
Already Have An Account? <a class="ml-2" href="{{ url_for('login') }}">Sign In</a>  
<!-- note that the login is not the route login but the function name on the  
route login. Take note of this -->  
</small>  
</div>  
{% endblock content %}
```

Now the login template, we basically will copy the entire code of the register.html and modify the content, remember that we only need the email and the password to login so all every field properties will be removed
```html
{% extends "layout.html" %}  
{% block content %}  
<div class="content-section">  
<form action="" method="POST">  
{{ form.hidden_tag() }}  
<fieldset class="form-group"> <!--this is a bootstrap class -->  
<legend class="border-bottom mb-4">Login</legend>  
<!-- the mb-4 is simply a margin bottom of 4 -->  
  
<div class="form-group">  
{{ form.email.label(class='form-control-label') }}  
  
{% if form.email.errors %}  
{{ form.email(class='form-control form-control-lg is-invalid') }}  
<div class="invalid-feedback">  
{% for error in form.email.errors %}  
<span>{{ error }}</span>  
{% endfor %}  
</div>  
{% else %}  
{{ form.email(class='form-control form-control-lg') }}  
{% endif %}  
  
</div>  
<div class="form-group">  
{{ form.password.label(class='form-control-label') }}  
{% if form.password.errors %}  
{{ form.password(class='form-control form-control-lg is-invalid') }}  
<div class="invalid-feedback">  
{% for error in form.password.errors %}  
<span>{{ error }}</span>  
{% endfor %}  
</div>  
{% else %}  
{{ form.password(class='form-control form-control-lg') }}  
{% endif %}  
</div>  
<div class="form-check">  
{{ form.remember(class="form-check-input") }}  
{{ form.remember.label(class="form-check-label") }}  
</div>  
<!-- lets add a link for forget password -->  
  
<div class="form-group">  
{{ form.submit(class='btn btn-outline-info') }}  
</div>  
<small class="text-muted ml-2">  
<a href="#">forget password?</a>  
</small>  
</fieldset>  
</form>  
</div>  
<div class="border-top pt-3">  
<small class="text=muted">  
Need An Account? <a class="ml-2" href="{{ url_for('register') }}">Sign Up Now</a>  
<!-- note that the login is not the route login but the function name on the  
route login. Take note of this -->  
</small>  
</div>  
{% endblock content %}
```
Run the above code but before then, go through the code one after the other and try to understand the behind scene of this code
Now we need to update our flask to accept post and get request and as well validate the form.
```python 
@app.route("/login", strict_slashes=False, methods=['GET', 'POST'])  
def login():  
form = LoginForm()  
if form.validate_on_submit():  
if form.email.data == 'admin@blog.com' and form.password.data == 'admin':  
flash('You have been logged in!', 'success')  
return redirect(url_for('home'))  
else:  
flash('Login Unsuccessful, Check your login details or sign-up', 'danger')  
return render_template("login.html", title="Login", form=form)
```
In the above code, we have hard-coded an email as data and password as well since we are yet to setup a database, we assume that a successful login will remain the above values and every other attempt is invalid. The danger is a bootstrap definition of an unsuccessful attempt to login.