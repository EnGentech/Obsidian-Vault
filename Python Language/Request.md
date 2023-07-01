The header in get() could take the underlisted parameters
In an HTTP request, the `HEAD` method is used to retrieve the headers of a resource without requesting the actual content of the resource. The response to a `HEAD` request contains only the headers and not the body of the resource.

The available headers in an HTTP request can vary depending on the specific use case and the server configuration. However, there are several commonly used headers that you can include in an HTTP request:

1. `Accept`: Specifies the media types that are acceptable in the response, typically used to request a specific content type (e.g., `Accept: application/json`).
    
2. `Authorization`: Provides credentials to authenticate the client with the server, often used with authentication mechanisms like Basic or Bearer tokens.
    
3. `Content-Type`: Specifies the media type of the data sent in the request body (e.g., `Content-Type: application/json`).
    
4. `User-Agent`: Identifies the client making the request, typically used by servers to determine how to format the response or track usage statistics.
    
5. `Cookie`: Contains previously stored cookies that the server can use to maintain session information.
    
6. `Cache-Control`: Specifies caching directives for the request or response, controlling how caching should be handled by intermediate caches.
    
7. `Referer`: Indicates the URL of the previous web page from which the current request originated, commonly used for tracking or redirecting purposes.
    
8. `If-Modified-Since`: Allows conditional retrieval of a resource based on the last-modified timestamp, used with the value of the `Last-Modified` header from a previous response.
    
9. `Range`: Specifies a range of bytes to retrieve from a resource, commonly used for partial content requests or resumable downloads.

## Python API
```python
#!/usr/bin/python3  
"""Get the first 10 commit messages"""  
  
import requests  
from sys import argv  
  
if __name__ == '__main__':  
owner = argv[2]  
repo = argv[1]  
url = 'http://api.github.com/repos/{}/{}/commits'.format(repo, owner)  
  
header = {  
'Accept': 'application/vnd.github+json'  
}  
  
content = requests.get(url, headers=header).json()  
  
count = 1  
for x in content:  
print('{}: {}'.format(x['sha'], x['author name']))  
count += 1  
if count == 10:  
break  
  
# Coded by EnGentech  
  
#token = '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'
```