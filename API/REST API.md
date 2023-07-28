link: [(140) APIs for Beginners 2023 - How to use an API (Full Course / Tutorial) - YouTube](https://www.youtube.com/watch?v=WXsD0ZgxjRw)

```python
from flask import Flask, request, jsonify  
  
app = Flask(__name__)  
  
book_list = [  
{  
'id': 1,  
'author': "Gentle",  
'language': "English",  
'title': "EnGentech, the pride of time"  
},  
{  
'id': 2,  
'author': "Chime",  
'language': "Spanish",  
'title': "Talu Escasor"  
}  
]  
  
@app.route("/books", methods=["GET", "POST"])  
def books():  
if request.method == "GET":  
if len(book_list) > 0:  
return jsonify(book_list)  
else:  
return "Nothing in list", 404  
  
if request.method == 'POST':  
new_author = request.form['author']  
new_language = request.form['language']  
new_title = request.form['title']  
iD = book_list[-1]['id']+1 # this is the id of the previous book list  
  
new_obj = {  
'id': iD,  
'author': new_author,  
'language': new_language,  
'title': new_title  
}  
# Lets append the list to the previous  
  
book_list.append(new_obj)  
#then return the file in json  
return jsonify(book_list), 201  
  
# Note tha we are using an in-memory list which will only be available only on runtime,  
# This is to say that the storage ability is not permanent as we are not populating  
# the list in a database where the information can later be retrived  
  
if __name__ == "__main__":  
app.run(debug=True)
```
Am sorry that I lost the content that explained the above. but in a quick view, lets see to the importation of the above. from flask we imported Flask, request and jsonified
reason being that
1. Flask is used to get the instance of the flask class
2. request is used to connect to the web Api
3. jsonified is used to create a json string from or of the data pushed to or received from the web api

Lets create a flask code that returns the object based on input provided via the url as id. If the provided id is not available, the return should be  Id: id not available using the route ("/books/<int:id>")

```python
from flask import Flask, request, jsonify  
  
app = Flask(__name__)  
  
book_list = [  
{  
'id': 1,  
'author': "Gentle",  
'language': "English",  
'title': "EnGentech, the pride of time"  
},  
{  
'id': 2,  
'author': "Chime",  
'language': "Spanish",  
'title': "Talu Escasor"  
}  
]  
  
@app.route("/books", methods=["GET", "POST"])  
def books():  
if request.method == "GET":  
if len(book_list) > 0:  
return jsonify(book_list)  
else:  
return "Nothing in list", 404  
  
if request.method == 'POST':  
new_author = request.form['author']  
new_language = request.form['language']  
new_title = request.form['title']  
iD = book_list[-1]['id']+1 # this is the id of the previous book list  
  
new_obj = {  
'id': iD,  
'author': new_author,  
'language': new_language,  
'title': new_title  
}  
# Lets append the list to the previous  
  
book_list.append(new_obj)  
#then return the file in json  
return jsonify(book_list), 201  
  
# Note tha we are using an in-memory list which will only be available only on runtime,  
# This is to say that the storage ability is not permanent as we are not populating  
# the list in a database where the information can later be retrived  
  
@app.route("/books/<int:id>", methods=['GET', 'PUT', 'DELETE'])  
def book_id(id):  
if request.method == "GET":  
for x in book_list:  
if x['id'] == id:  
return jsonify(x)  
else:  
return "Id: {} is not available".format(id)  
  
elif request.method == "PUT":  
for x in book_list:  
if x['id'] == id:  
x['author'] = request.form['author']  
x['language'] = request.form['language']  
x['title'] = request.form['title']  
new_update = {  
'id': id,  
'author': x['author'],  
'language': x['language'],  
'title': x['title']  
}  
return jsonify(new_update)  
  
elif request.method == "DELETE":  
for key, value in enumerate(book_list):  
if key == id - 1:  
book_list.pop(key)  
return jsonify(book_list)  
  
  
if __name__ == "__main__":  
app.run(debug=True)
```

The above code will only be functional as at the moment it is running in an in-memory list to store our data which is only viewable via a session, once the session is over or closed, it resets hence the use of db for storage is essential.

## Working with database
