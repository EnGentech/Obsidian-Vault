link: [flask_cheatsheet.pdf](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/301/flask_cheatsheet.pdf)

## Building API's
building an API with flask, three important methods are essential, 
1. Flask for creating an instance of the class
2. request for sending an http request 
3. jsonify for composing the response into a JSON file system

lets use a certain code to explain the concept of creating an API
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
			  
]

@app.route('/books', methods=['GET', 'POST'])

```
From the above basic concept, we have a list of books in the directory, we use the GET request to return the list of books to the client and if the request method is POST, we update the content of the book list. However, we can get some information from the user before populating the content of the books.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
			  
]

@app.route('/books', methods=['GET', 'POST'])
def books():
if request.method == "GET":
if len(book_list) > 0:
return jsonify(books_list)
else:
"Nothing Found", 404

if request.method == "POST":
new_author = request.form['author']
new_lang = request.form['language']
new_title = request.form['title']
```

Having the above, we will now generate a dictionary via the collected items and add to our list previously defined if any

The new code becomes 
```python
from flask import Flask, request, jsonify  
  
app = Flask(__name__)  
  
book_list = [  
  
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
app.run()
```

