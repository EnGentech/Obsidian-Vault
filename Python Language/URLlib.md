link: [urllib.parse — Parse URLs into components — Python 3.11.4 documentation](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse)
good resource: [Python's urllib.request for HTTP Requests – Real Python](https://realpython.com/urllib-request/)
get web content with the code 
```python 
#!/usr/bin/python3  
"""Get the content from https://alx-intranet.hbtn.io/status  
and display in a certain way as seen below  
Body response:$  
- type: <class 'bytes'>$  
- content: b'OK'$  
- utf8 content: OK$  
"""  
import urllib.request  
if __name__ == "__main__":  
with urllib.request.urlopen('https://alx-intranet.hbtn.io') as rqst:  
html = rqst.read()  
  
utf_content = html.decode('utf-8')  
content = html  
clas = html.__class__  
print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"  
.format(clas, content, utf_content))  
# Coded by EnGentech
```

Source code of a page can be gotten using the short cut key ctrl + u after inputting the url in the address bar
## The GET request
when you look at the web page, you will notice the ? with a key value pair attached to it, this is seen a variable to a value same as dictionary in python
```python
#!/usr/bin/python3  
"""Get a response message from the server  
with a query string passed to the server  
basically an email  
"""  
import urllib.request  
import sys  
  
if __name__ == "__main__":  
get_val = 'X-Request-Id'  
url = sys.argv[1]  
with urllib.request.urlopen(url) as file:  
con = file.headers.get(get_val)  
  
print(con)  
  
# Coded by EnGentech
```

## Methods used in websites
```python
from urllib.request import urlopen  
import pprint  
  
with urlopen("https://heritagepoly.edu.ng/eportals/dashboard.php") as req:  
file = req.read()  
  
pprint.pprint(dir(file))
```

## Header content can be gotten such
```python
from urllib.request import urlopen  
import pprint  
  
with urlopen("https://heritagepoly.edu.ng/eportals/dashboard.php") as req:  
file = req.headers  
  
pprint.pprint(file.items())
```

## Converting the byte to string by means of decoding
```python
from urllib.request import urlopen  
import pprint  
  
with urlopen("https://heritagepoly.edu.ng/eportals/dashboard.php") as req:  
file = req.read()  
  
lis = file.decode('utf-8')  
print(lis)
```
and better of using the header content charset
```python
from urllib.request import urlopen  
with urlopen("https://www.example.com") as response:  
body = response.read()  
character_set = response.headers.get_content_charset()  
  
print(character_set)  
  
decoded_body = body.decode(character_set)  
print(decoded_body[:30])
```

## Write into a HTML file
```python
from urllib.request import urlopen  
with urlopen("https://www.example.com") as response:  
body = response.read()  
character_set = response.headers.get_content_charset()  
  
print(character_set)  
  
decoded_body = body.decode(character_set)  
print(decoded_body[:30])  
  
  
# Write the above into a file  
with open("index.html", mode='wb') as html_file:  
html_file.write(body)
```

## Handling Errors
```python
from urllib.request import urlopen  
with urlopen("https://www.example.com") as response:  
body = response.read()  
character_set = response.headers.get_content_charset()  
  
print(character_set)  
  
decoded_body = body.decode(character_set)  
print(decoded_body[:30])  
  
  
# Write the above into a file  
with open("index.html", mode='wb') as html_file:  
html_file.write(body)
```

```python 
#!/usr/bin/python3  
"""Get a response message from the server  
with a query string passed to the server  
basically an email  
"""  
from urllib import request, parse, error  
import sys  
  
if __name__ == "__main__":  
try:  
url = "http://www.engentech.tech"  
with request.urlopen(url) as response:  
content = response.read().decode("utf-8")  
print(content)  
except error.HTTPError as err:  
print("Error code: {}".format(err.status))  
  
# Coded by EnGentech
```

To run a code or function consistently, you can run your python with a flag of i to make it an interactive shell
```python
python -i file_name
```
