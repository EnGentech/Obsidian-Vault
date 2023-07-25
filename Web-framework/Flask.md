flask installation guide: [Installation — Flask Documentation (2.1.x) (palletsprojects.com)](https://flask.palletsprojects.com/en/2.1.x/installation/)
documentation link: https://flask.palletsprojects.com/en/2.3.x/quickstart/

Guides:
flask is a micro web framework other than django, this implies that it does not have as much feature for a full blown web application like that of django and the likes. however its good practice to learn from. It can be applied at the front end and at the back end respectively.
the first thing to do is to install flask using the simple command line
```terminal
pip install flask
```
However, its best practice to install flask using environment known as venv. to do this, the above link provides detail information on that. 

Next, lets run a basic flask application
```python
from flask import Flask
#where the Flask is the class imported
#After the import, create an instance of the Flask web application
app = Flask(__main__) #or __name__ depending on the version in use
# lets run the script and see the result
if __name__ == '__main__':
app.run()

```
Running the above will not yield any result although the web app will start using a local server IP.  now lets add a page content to the above code
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
#the above line describes where the page will lunch from, that decorator specifies the path at which the program will be called, in this case, the program will be called immediately after the / which implies that it will be called as the index page
def home():
return "This is homepage for <h1>EnGentech</h1>"
#Note that we could use html tags within this context, this will be covered in later documentations
if __name__ == '__main__':
app.run()
```
Lets add another page to the previous
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
return "This is homepage for <h1>EnGentech</h1>"

@app.route("/<name>")
def user(name):
return "This is {}".format(name)
# In the above example, the function gets a value from user but already the route(...) specifies that what ever path_name associated to the root /, the name will be captured and printed to the web page. example if the input on the url is 127.0.0.1:5000/EnGentech, the name EnGentech will be printed

if __name__ == '__main__':
app.run()
```

One more thing in here

## The Redirection
take an instance of you entering password to login to a certain site and its not authenticated, such person could be redirected to the home screen or some other. Let look at the very basic of this
```python
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def home():
return "This is homepage for <h1>EnGentech</h1>"

@app.route("/<name>")
def user(name):
return "This is {}".format(name)

@app.route("/admin")
def admin():
return redirect(url_for("home"))

if __name__ == '__main__':
app.run()
# In the above code, the redirect simply return a specified page to the user is a criteria is not meet. in addition, the redirect and the url_for must be imported in other to use this concept.
#From the above, anytime the path /admin is entered into the web url, it will simply redirect the user to the home page since theres was no good rules applied in it
```

## Template
On template, its quite better to create all your template files in a folder called template within the same directory with other of your python scripts. In this case, we will create a folder named templates.

First, we will create a basic html file called index.html. this will be called up using the render_template method in flask. To do this, we will write a basic html code inside the templates 
directory.

Note that the directory name templates is basically used as it is used by default in flask to search for templates. if the name is not defined as templates, then some other measures needs to be put in place for flask to acknowledge the folder where the file is located
```html
Basic code with Home Page! content
```

```python
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
return render_template("index.html", content="Testing")

if __name__ == "__main__":
app.run()
```

That was pretty cool but that not the only essentials of using flask template, there are other varieties of things that can be done using flask template which could be cool. 
Lets say we want to render a dynamic content to the user. Lets say we want to display name as we did before from the backend to the front end. we can do this..
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
return render_template("index.html")

if __name__ == "__main__":
app.run()
```

In the front end, there will be a little modification. that is to create a variable that will store the name tendered from the backend to the front end using two curly braces as {{variable_name}}. The code will look like
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home page</title>
</head>
<body>
    <p>Welcome {{content}}</p>
</body>
</html>
```
then we add the variable to the backend and assign what ever value that will be displayed in the front end. In this case, we are dealing with the name 
The new python code for flask will become:
```python
from flask import Flask, redirect, url_for, render_template  
from os import path  
  
check = "template/index.html"  
if path.exists(check):  
print("Ok")  
else:  
print("not found")  
app = Flask(__name__)  
  
@app.route("/<name>")  
def home(name):  
return render_template("index.html", content=name)  
  
if __name__ == "__main__":  
app.run()
```

from the above, if you enter a url like, 127.0.0.1:5000/EnGentech, the web content will become 
Welcome EnGentech

You can pass multiple content, example we can pass content = value, another_content=value etc. All that is passed here should have a place where it reflects on the front end. ie. HTML file
We also can ren some python codes in html that will allow us to do some stuff as if it was python using the {% %} syntax, in the below example we are going to print hello and engentech for 10 times but with condition. 
All positive iterations should print Hello while odd prints EnGentech
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home page</title>
</head>
<body>

    <p>Welcome {{content}}</p>
    <p>Let's print with python code</p>
    {% for x in range(10) %}
        {% if x % 2 == 0 %}
            <h2>Hello</h2>
        {% else %}
            <h3>EnGentech</h3>
            {% endif %}
    {% endfor %}
    
</body>
</html>
```
Note that the {{}} is used to pass variable into the html file

Lets look at another expression on this, lets create a list in the backend and populate same at the front end. In this case, 
```python
from flask import Flask, redirect, url_for, render_template  
from os import path  
  
check = "template/index.html"  
if path.exists(check):  
print("Ok")  
else:  
print("not found")  
app = Flask(__name__)  
  
@app.route("/")  
def index():  
return "This is index page"  
  
@app.route("/<name>")  
def home():  
return render_template("index.html", content=["EnGentech", "Angel", "solace", "Jewel"])  
  
if __name__ == "__main__":  
app.run()
```
We can note the list in the content variable above, now lets populate this list in the front end via the html file
```html
<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home page</title>
</head>
<body>

    <p>Welcome {{content}}</p>

    <p>Let's print with python code</p>

    {% for x in content %}

        <h2>{{x}}</h2>

    {% endfor %}

</body>
</html>
```
You can see how we used python concept to call the for loop where the {{x}} represents the variable that holds the list in the content populated from the back end

## Inheritance
In few example, there are times when we write a code for certain templates like a page with a certain page layout and styles, it will not be viable to repeat those codes assuming that is to the same across multiple pages of the web, here is where flask helps more, it inherits the template created and populate over a number of pages that require same template.
Lets create a simple theme to illustrate this using a new file in the templates folder named base.html
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
  
</body>  
</html>
```
Nothing yet is done, lets explain more: since this is the base template, we are not going to render it just yet. we are instead going to use this as a parent template to other child template at which the child is going to inherit from. take the index.html we created before to be the child template, this implies that the index.html can be configured to inherit the template which we are about to create.
If you remember the use of inheritance, this implies that the child process will make reference to all the snippets created in the parent and could modify certain things as well change some certain functionalities.
To allow the child template to make certain functionalities in the template, we utilize what we call a block. 
```html
<!doctype html>  
<html lang="en">  
<head>  
<meta charset="UTF-8">  
<meta name="viewport"  
content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">  
<meta http-equiv="X-UA-Compatible" content="ie=edge">  
<title>{% block title %} {% endblock %}</title>  
<!--the title is the name of the block-->
</head>  
<body>  
  
</body>  
</html>
```
in the above it implies that the child will give us content that we are going to fill into the block. lets head over to the child and make the changes
```html
{% extends "base.html" %}  
{% block title %} Home Page {% endblock %}
```
What the above does is that, it takes Home Page and substitute with what ever that was written into the base.html title. 
Now lets create a content that will be displayed across all pages and another block to define a content
```html
<!doctype html>  
<html lang="en">  
<head>  
<meta charset="UTF-8">  
<meta name="viewport"  
content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">  
<meta http-equiv="X-UA-Compatible" content="ie=edge">  
<title>{% block title %} {% endblock %}</title>  
<!--the title is the name of the block-->
</head>  
<body>  
  <h1>EnGentech</h1>
	{% block content %}
	{% endblock %}
</body>  
</html>
```
From the above, the block content represents the actual content of the web page, where the child process can overwrite the initial content defined in the parent html code. 
From the index.html code, we can add the block content with some html codes that will be rendered when the code is executed
```html
{% extends "base.html" %}  
{% block title %} Home Page {% endblock %}

{% block content %}
<h2>Test me</h2>
{% endblock %}
```
Now lets head to the python code.
Before we get started, we can define a parameter called debug inside the run function. this will enable auto update of the file just like live server in vscode. Lets do this first
```python
from flask import Flask, redirect, url_for, render_template  
  
app = Flask(__name__)  
  
@app.route("/")  
def index():  
return render_template("index.html", content="testing")  
  
if __name__ == "__main__":  
app.run(debug=True)
```
One will ask: why all this codes rather that adding the h1 tag to the index page which will be more simple, yes thats true but the essence of this code is basic learning, along the line, there will come some complex codes that needs not to be repeated at all time, hence the need for this codes experience. Lets forge ahead.
To continue, lets look at bootstrap. The bootstrap is simply a replica of css used in adding styling to your html in an easy way or method. to do this we get the css link and the js link from bootstrap.com. This will enable us to use some classes from classes written into bootstrap hence to make our styling easy to use
The link is in the code
```html
<!doctype html>  
<html lang="en">  
<head>  
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">  
<meta charset="UTF-8">  
<meta name="viewport"  
content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">  
<meta http-equiv="X-UA-Compatible" content="ie=edge">  
<title>{% block title %}{% endblock %}</title>  
</head>  
<body>  
<h1>Index page</h1>  
{% block content %}  
  
{% endblock %}  
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>  
</body>  
</html>
```

Lets now create a navbar that will be used in our parent code via bootstrap. all we need is to search navbar on bootstrap, get the code and use it in our base.html as seen below
```html
<!doctype html>  
<html lang="en">  
<head>  
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">  
<meta charset="UTF-8">  
<meta name="viewport"  
content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">  
<meta http-equiv="X-UA-Compatible" content="ie=edge">  
<title>{% block title %}{% endblock %}</title>  
</head>  
<body>  
<nav class="navbar navbar-expand-lg bg-body-tertiary">  
<div class="container-fluid">  
<a class="navbar-brand" href="#">Navbar</a>  
<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">  
<span class="navbar-toggler-icon"></span>  
</button>  
<div class="collapse navbar-collapse" id="navbarNav">  
<ul class="navbar-nav">  
<li class="nav-item">  
<a class="nav-link active" aria-current="page" href="#">Home</a>  
</li>  
<li class="nav-item">  
<a class="nav-link" href="#">Features</a>  
</li>  
<li class="nav-item">  
<a class="nav-link" href="#">Pricing</a>  
</li>  
<li class="nav-item">  
<a class="nav-link disabled">Disabled</a>  
</li>  
</ul>  
</div>  
</div>  
</nav>  
<h1>Index page</h1>  
{% block content %}  
  
{% endblock %}  
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>  
</body>  
</html>
```
Lets create a new file and inherit the parent code 
create a file called new and define a python flask route to point to new as seen below
```html
{% extends "base.html" %}
```
for now we dont need any other thing outside base.html since we are not modifying its content.
```python
from flask import Flask, redirect, url_for, render_template  
  
app = Flask(__name__)  
  
@app.route("/")  
def index():  
return render_template("index.html")  
  
@app.route("/test")  
def test():  
return render_template("new.html")  
  
if __name__ == "__main__":  
app.run(debug=True)
```

## Bootstrap link
[Get started with Bootstrap · Bootstrap v5.3 (getbootstrap.com)](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
continue: [(126) Flask Tutorial #4 - HTTP Methods (GET/POST) & Retrieving Form Data - YouTube](https://www.youtube.com/watch?v=9MHYHgh4jYc&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=4)

## Get/Post
Get is simply an insecure way of getting data to the client and post is a secure way of doing same.
From what we have been doing previously, you can observe that each time we run our url on the web browser, the console returns a get command on the interface because its not a secured option which implies that it can be seen out there. 
Using post is a secure way of sending an encrypted data that cannot be seen within the web browser usually data that will be send to the database. 
Lets make a little code for that
```python
from flask import Flask, redirect, url_for, render_template  
  
app = Flask(__name__)  
  
@app.route("/")  
def index():  
return render_template("index.html")  
  
@app.route("/login", methods=["POST", "GET"])  
def login():  
return render_template() 

@app.route("/<user>")
def user(user):
return user
  
@app.route("/test")  
def test():  
return render_template("new.html")  
  
if __name__ == "__main__":  
app.run(debug=True)
```
From the above, we can see the login declared with a method of POST and GET, basically the default value is the GET method except specified, we are using both POST and GET because we will be using the two in the cause of this our program. 
In the render_template, it is noted that it is empty, thats because, we will create a template to use within that context. 
Create a new html template known as login
```html
{% extends "base.html" %}  
{% block title %} Login Page {% endblock %}  
{% block content %}  
<form action="#" method="post">  
<p>Name:</p>  
<p><input type="text" name="nm"></p>  
<p><input type="submit" value="submit"></p>  
</form>  
{% endblock %}
```
In there we have a form which is use to collect information from user and send it to the server. the form has the action which specifies the IP at which the content will be redirected to and the method determines the way at which the information will be submitted.  Now lets add this html file to be rendered to the previous python script code. We will consider only that very line of code
```python
@app.route("/login", methods=["POST", "GET"])  
def login():  
return render_template("login.html")
```

The next step is to figure how to get the information inputted by user and handle it from the backend but before that run the code to ensure everything is working fine
Notice that when you click on submit button on the screen if properly rendered will return POST method instead of the default GET. In addition, notice that the URL indicates also the # tendered in the action attribute of the html code. The # there is used when we are submitting our form to the same page (works like anchor)

Next we need to determine if what we are rendering the POST request or the GET request. to do this we will import the request from the flask module. to do that we use an if statement
```python
from flask import Flask, redirect, url_for, render_template, request  
  
app = Flask(__name__)  
  
@app.route("/")  
def index():  
return render_template("index.html")  
  
@app.route("/login", methods=["POST", "GET"])  
def login():  
if request.method == "POST":  
user = request.form['nm']  
return redirect(url_for("user", user=user))  
else:  
return render_template("login.html")  
  
@app.route("/<user>")  
def user(user):  
return user  
  
@app.route("/test")  
def test():  
return render_template("new.html")  
  
if __name__ == "__main__":  
app.run(debug=True)
```
In the above, we use the if else statement to determine the method used in the request, In this context, we check if the POST method is used (the submit button is clicked), we create a variable known as user the get the name passed by the form by using the name value from the form as a key to get the value (user = request.form['nm']). If POST method, the page redirect us to user and serve the name provided as a value to the user route, however, if nothing is passed, the home path will be utilized.

## Sessions
A session is simply a mean of creating a memory block for the server to remember the login user on the net without having to login at every instance of visiting pages. Take for instance, if you log into facebook, you can navigate to different pages without having to re-log in as long as you have not logged out, this is done using session. Lets create a simple code to illustrate this with a route called user in the python flask
```python
from flask import Flask, redirect, url_for, render_template, request, session  
  
app = Flask(__name__)  
app.secret_key = "hello"  
  
@app.route("/")  
def index():  
return render_template("index.html")  
  
@app.route("/login", methods=["POST", "GET"])  
def login():  
if request.method == "POST":  
user = request.form['nm']  
session['user'] = user  
return redirect(url_for("user"))  
else:  
return render_template("login.html")  
  
@app.route("/user")  
def user():  
if "user" in session:  
user = session['user']  
return "You are logged in as {}".format(user)  
else:  
return render_template("login")  
  
@app.route("/test")  
def test():  
return render_template("new.html")  
  
if __name__ == "__main__":  
app.run(debug=True)
```
In the above, we created a session for the user. Note that when creating a session, you must specify a secret key for the encryption, ensure to use something complicated rather than the hello used for the purpose of this article.
```python
from flask import Flask, redirect, url_for, render_template, request, session  
  
app = Flask(__name__)  
app.secret_key = "hello"  
  
@app.route("/")  
def index():  
return render_template("index.html")  
  
@app.route("/login", methods=["POST", "GET"])  
def login():  
if request.method == "POST":  
users = request.form['nm']  
session['user'] = users  
return redirect(url_for("user"))  
else:  
return render_template("login.html")  
  
@app.route("/user")  
def user():  
if "user" in session:  
use = session['user']  
return "You are logged in as {}".format(use)  
else:  
return redirect(url_for("login"))  
  
@app.route("/test")  
def test():  
return render_template("new.html")  
  
if __name__ == "__main__":  
app.run(debug=True) 
```
Lets see how to logout
This is simply done using session.pop() method.
```python
from flask import Flask, redirect, url_for, render_template, request, session  
  
app = Flask(__name__)  
app.secret_key = "hello"  
  
@app.route("/")  
def index():  
return render_template("index.html")  
  
@app.route("/login", methods=["POST", "GET"])  
def login():  
if request.method == "POST":  
users = request.form['nm']  
session['user'] = users  
return redirect(url_for("user"))  
else:  
if "user" in session:  
return redirect(url_for("user"))  
return render_template("login.html")  
  
@app.route("/logout")  
def logout():  
session.pop('user', None)  
return redirect(url_for("login"))  
  
@app.route("/user")  
def user():  
if "user" in session:  
use = session['user']  
return "You are logged in as {}".format(use)  
else:  
return redirect(url_for("login"))  
  
@app.route("/test")  
def test():  
return render_template("new.html")  
  
if __name__ == "__main__":  
app.run(debug=True)
```
With this, when the logout is applied, the user will be logged out and deleted from the session, however, if you try to access /user on the url, you will be redirected to the login page since no session is active. The none used in the session.pop is used to return none if the user is not found in the dictionary. 
You also notice that we added an if statement in the else block of the login, that is used to redirect us to the user page if there exist a session else you have to logout first. Take an instance of facebook, when you login into your account in you laptop, you cant log in another except the former is logged out, thats the same implementation here in a simple interface.
However, there's a limitation. If you close your web browser and reload again, the session will be closed, remember that if you close your web browser in terms of facebook and login again, you will still be logged in without having to log in from the beginning. By this we can user permanent session to do this. by using permanent session, you will validate the duration at which you need this to happen, take you mind to persistence cookies and temporarily cookies, they work almost the same.
The improved code becomes
```python 
from flask import Flask, redirect, url_for, render_template, request, session  
from datetime import timedelta  
  
app = Flask(__name__)  
app.secret_key = "hello"  
app.permanent_session_lifetime = timedelta(days=3)  
  
@app.route("/")  
def index():  
return render_template("index.html")  
  
@app.route("/login", methods=["POST", "GET"])  
def login():  
if request.method == "POST":  
session.permanent = True  
users = request.form['nm']  
session['user'] = users  
return redirect(url_for("user"))  
else:  
if "user" in session:  
return redirect(url_for("user"))  
return render_template("login.html")  
  
@app.route("/logout")  
def logout():  
session.pop('user', None)  
return redirect(url_for("login"))  
  
@app.route("/user")  
def user():  
if "user" in session:  
use = session['user']  
return "You are logged in as {}".format(use)  
else:  
return redirect(url_for("login"))  
  
@app.route("/test")  
def test():  
return render_template("new.html")  
  
if __name__ == "__main__":  
app.run(debug=True)
```
From the above, we imported the timedelta which we use to specify the days our session should be active, we can set in minutes, seconds etc. then secondly turn our session.permanent = True. With this, even if a user closes the web browser and reloads, he will still be active except after 3 days as specified here or he logs out

## Message Flashing
This is simply reflecting a message from the previous page to the new page when something happens. e.g, if a user login, in the new page we could write login successfully and same when the user logs out. First we will modify our python scripts and then modify the html script as seen below
```python
from flask import Flask, flash, redirect, url_for, render_template, request, session  
from datetime import timedelta  
  
app = Flask(__name__)  
app.secret_key = "hello"  
app.permanent_session_lifetime = timedelta(days=3)  
  
@app.route("/")  
def index():  
return render_template("index.html")  
  
@app.route("/login", methods=["POST", "GET"])  
def login():  
if request.method == "POST":  
session.permanent = True  
users = request.form['nm']  
session['user'] = users  
return redirect(url_for("user"))  
else:  
if "user" in session:  
return redirect(url_for("user"))  
return render_template("login.html")  
  
@app.route("/logout")  
def logout():  
session.pop('user', None)  
flash("You have been logged out", "info")  
return redirect(url_for("login"))  
  
@app.route("/user")  
def user():  
if "user" in session:  
use = session['user']  
return "You are logged in as {}".format(use)  
else:  
return redirect(url_for("login"))  
  
@app.route("/test")  
def test():  
return render_template("new.html")  
  
if __name__ == "__main__":  
app.run(debug=True)
```

```html
{% extends "base.html" %}  
{% block title %} Login Page {% endblock %}  
{% block content %}  
{% with messages = get_flashed_messages() %}  
{% if messages %}  
{% for msg in messages %}
<p>{{ msg }}</p>  
{% endfor %}  
{% endif %}  
{% endwith %}  
<form action="#" method="post">  
<p>Name:</p>  
<p><input type="text" name="nm"></p>  
<p><input type="submit" value="submit"></p>  
</form>  
{% endblock %}
```
in the html file, we use the with method to get whatever flashed messages populated from the backend, we then use the if statement to check if there exist any message, in case they are more than one, we iterate through them and render the message using the p tag

Notice from the previous that you have been logged out is viewable on the web browser but the issue could be that you will always see this message each time the logout directory is called upon instead of when someone actually logs out. to do this, we need to display the massage only when there an active user who just logged out. hence the next code
```python
from flask import Flask, flash, redirect, url_for, render_template, request, session  
from datetime import timedelta  
  
app = Flask(__name__)  
app.secret_key = "hello"  
app.permanent_session_lifetime = timedelta(days=3)  
  
@app.route("/")  
def index():  
return render_template("index.html")  
  
@app.route("/login", methods=["POST", "GET"])  
def login():  
if request.method == "POST":  
session.permanent = True  
users = request.form['nm']  
session['user'] = users  
return redirect(url_for("user"))  
else:  
if "user" in session:  
return redirect(url_for("user"))  
return render_template("login.html")  
  
@app.route("/logout")  
def logout():  
if "user" in session:  
logout_user = session["user"]  
flash("You have been logged out @ {}".format(logout_user), "info")  
session.pop('user', None)  
return redirect(url_for("login"))  
  
@app.route("/user")  
def user():  
if "user" in session:  
use = session['user']  
return "You are logged in as {}".format(use)  
else:  
return redirect(url_for("login"))  
  
@app.route("/test")  
def test():  
return render_template("new.html")  
  
if __name__ == "__main__":  
app.run(debug=True)
```

## Using SQLAlchemy Database
This video will base more on working with databases, sending information to databases and doing some stuffs in it. first install sqlalchemy is you dont have it install.
For this very task, we will create a means whereby a user can enter his email, modify it or delete if from the database
In our python script, we will update few things, first by importing sqlalchemy and other stuffs
```python
from flask import Flask, flash, redirect, url_for, render_template, request, session  
from datetime import timedelta  
from flask_sqlalchemy import sqlalchemy 
  
app = Flask(__name__)  
app.secret_key = "hello"  
app.permanent_session_lifetime = timedelta(days=3)  
  
@app.route("/")  
def index():  
return render_template("index.html")  
  
@app.route("/login", methods=["POST", "GET"])  
def login():  
if request.method == "POST":  
session.permanent = True  
users = request.form['nm']  
session['user'] = users  
return redirect(url_for("user"))  
else:  
if "user" in session:  
return redirect(url_for("user"))  
return render_template("login.html")  
  
@app.route("/logout")  
def logout():  
if "user" in session:  
logout_user = session["user"]  
flash("You have been logged out @ {}".format(logout_user), "info")  
session.pop('user', None)  
session.pop('email', None)  
return redirect(url_for("login"))  
  
@app.route("/user", methods=["POST", "GET"])  
def user():  
email = None  
if "user" in session:  
use = session['user']  
  
if request.method == 'POST':  
email = request.form['email']  
session['email'] = email  
flash("Email was saved!", 'info')  
else:  
if 'email' in session:  
email = session['email']  
  
return render_template("user.html", email=email)  
else:  
flash("You are not logged in!")  
return redirect(url_for("login"))  
  
@app.route("/test")  
def test():  
return render_template("new.html")  
  
if __name__ == "__main__":  
app.run(debug=True)
```
Just as when we created the user with a session and a flash message, we do same with the email. and we create a user.html file with a form that will request a user to input his email
In the next phase, we will see how to work with databases
Notice that the import in line three is not yet used as we will cover that in the next phase
```html
{% extends "base.html" %}  
{% block title %} User {% endblock %}  
{% block content %}  
{% with messages = get_flashed_messages() %}  
{% if messages %}  
{% for msg in messages %}  
<p>{{ msg }}</p>  
{% endfor %}  
{% endif %}  
{% endwith %}  
<form action="#" method="POST">  
<input type="email" name="email" placeholder="Enter email" value="{{email if email}}">  
<input type="submit" value="Submit">  
</form>  
{% endblock %}
```
The form uses the POST method to send request, in the second line, the placeholder is used as a default value to be written on the field which will be deleted automatically when a value is entered into the field, and the value is used to write the actual email in replacement of the placeholder if there exist any email

## Working our with databases
There are varieties of option to utilize when it comes to working with databases. we can use mysqldb, lite, etc, for this tutorial, we are using flask_sqlalchemy which implies that it should be installed if not already installed. 
```python
from flask import Flask, flash, redirect, url_for, render_template, request, session  
from datetime import timedelta  
from flask_sqlalchemy import SQLAlchemy  
  
app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3' # users here refers  
# the table while others are just the configuration code  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
# the above line removes warnings we get sometimes and its optional  
app.secret_key = "hello"  
app.permanent_session_lifetime = timedelta(days=3)  
  
db = SQLAlchemy(app) # this creates a db  
  
# Lets create a model for our database  
class users(db.Model):  
_id = db.Column("id", db.Integer, primary_key=True)  
name = db.Column(db.String(100))  
email = db.Column(db.String(100))  
  
def __init__(self, name, email):  
self.name = name  
self.email = email  
  
@app.route("/")  
def index():  
return render_template("index.html")  
  
@app.route("/login", methods=["POST", "GET"])  
def login():  
if request.method == "POST":  
session.permanent = True  
users = request.form['nm']  
session['user'] = users  
return redirect(url_for("user"))  
else:  
if "user" in session:  
return redirect(url_for("user"))  
return render_template("login.html")  
  
@app.route("/logout")  
def logout():  
if "user" in session:  
logout_user = session["user"]  
flash("You have been logged out @ {}".format(logout_user), "info")  
session.pop('user', None)  
session.pop('email', None)  
return redirect(url_for("login"))  
  
@app.route("/user", methods=["POST", "GET"])  
def user():  
email = None  
if "user" in session:  
use = session['user']  
  
if request.method == 'POST':  
email = request.form['email']  
session['email'] = email  
flash("Email was saved!", 'info')  
else:  
if 'email' in session:  
email = session['email']  
  
return render_template("user.html", email=email)  
else:  
flash("You are not logged in!")  
return redirect(url_for("login"))  
  
@app.route("/test")  
def test():  
return render_template("new.html")  
  
if __name__ == "__main__":  
db.create_all()  
# this is used to create the database and its essential to write it above the app.run
app.run(debug=True)
```
The above code comes with comment to explain each new line of items added to the python script. Actually thats the basic configuration, now lets look into creating a means whereby we check in the database to see if a user already exist otherwise we create one and also do other stuffs.
```python
```

