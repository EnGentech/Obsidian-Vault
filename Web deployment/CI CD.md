The lean/agile methodology (See: [Twelve Principles of Agile Software](https://intranet.alxswe.com/rltoken/nAIKs38-2F3SWHulrmAZ8g "Twelve Principles of Agile Software")) is now widely used by the industry and one of its key principles is to iterate as fast as possible. If you apply this to software engineering, it means that you should:

- code
- ship your code
- measure the impact
- learn from it
- fix or improve it
- start over

As fast as possible and with small iterations in days or even hours (whereas it used to be weeks or even months). One big advantage is that if product development is going the wrong direction, fast iteration will allow to quickly detect this, and avoid wasting time.

From a technical point of view, quicker iterations mean fewer lines of code being pushed at every deploy, which allows easy performance impact measurement and easy troubleshooting if something goes wrong (better to debug a small code change than weeks of new code).

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/75dbe73200b7537f462b0dd81ad010b7840436d8.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230705T113059Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8fdfb3f1aff140c0a0d0d8f3014708f7cf63dd93ff1ded2e9c02eb11dcdab3a1)

Applied to software engineering, [CI/CD](https://intranet.alxswe.com/rltoken/3UPNbDpVhYUm9KhQNkitjw "CI/CD") (Continuous Integration/Continuous Deployment) is a principle that allows individuals or teams to have a lean/agile way of working.

This translates to a “shipping pipeline” which is often built with multiple tools such as:

- Shipping the code:
    - Capistrano, Fabric
- Encapsulating the code
    - Docker, Packer
- Testing the code
    - Jenkins, CircleCi, Travis
- Measuring the code
    - Datadog, Newrelic, Wavefront


## Functions in fab
## Fabric functions

```python
Fabric provides a set of commands in fabric.api that are simple but powerful.

With Fabric, you can use simple Fabric calls like
```

```python
local	# execute a local command)
run	# execute a remote command on all specific hosts, user-level permissions)
sudo	# sudo a command on the remote server)
put	# copy over a local file to a remote destination)
get	# download a file from the remote server)
prompt	# prompt user with text and return the input (like raw_input))
reboot	# reboot the remote system, disconnect, and wait for wait seco
```
link: [How to use Fabric in Python - PythonForBeginners.com](https://www.pythonforbeginners.com/systems-programming/how-to-use-fabric-in-python)

## local command

the local command is used to create local commands that takes up your linux commands and create its own command based on definition of functions. this is achieveable using the python function process to automate your desired local function. e.g
```python
from fabric import *

def saymyname()
	local('whoami')

#Remember that, whoami is a linux command hence running this is equivalent to utilizing the command whoami on the stdout. however you can list the command available, or the commands you created using the command line below. 

# In addition, some versions of fabric wont work like this hence the importation should include api so we have

from fabric.api import *

def saymyname():
	local('whoami')

saymyname()

```
```linux
fab --list
```

## The Run command
Using the local command runs any command invoked locally within the system, but if you are to run the command on a remote server, you use the run command but in here you will have to specify the connection to the server you are to run the command. for instance if you run this
```python
from fabric.api import *

def myname():
	run('whoami')

myname()
# In here, the program will return a comment that no connection to a remote host was made, hence we may need to make the connections first
```

## Basic Connection to User-Server
```python
# on a lighter mode, lets connect to our server and print the user name 

from fabric import Connection
connection = Connection(Host = 'ubuntu@engentech.tech')

connection
```

Note that the above method is used for the updated version of fabric, for users below this upgrade will have to use the env variable to connect as seen below
```python
#!/usr/bin/python3

from fabric.api import *
#from fabric import Connection

def myserver():
    env.host_string = 'ubuntu@your_ip or your_domain'

myserver()

def myname():
    run('whoami')

myname()
```

running the dir option prints all the possible ability of the connection  that is connected to the host 
```python 
print(dir(connection))
```

Fabric is basically for executing command on ssh unto a remote host. if the host is connected using a password, then the connection will feature one more argument call connect_kwargs
```python
from fabric import Connection
# the above imports the Connection class from fabric
connection = Connection(host = 'ubuntu@engentech.tech', connect_kwargs = {'password': "mypassword"})
```

## Getting a formatted output
```python
import fabric  
  
connection = fabric.Connection(host = 'ubuntu@engentech.tech')  
result = connection.run("whoami")  
#print(dir(connection))  
  
print(f'Ran command: {result.command!r} on {result.connection.host} with'f'result: {result.stdout}')
# note that the !r add the '' to the command when printed, in this case, the whoami linux command will be printed to the screen with a '' surrounding it
```

However, the above concept wont be used when running a command that required sudo privilege example, if sudo is added to the command above such that we have sudo whoami, this will return an exception hence the next line of adjustment in the code

## Running Sudo command 
Before diving into this, lets start by defining a basic way of creating a function to automate things for us
In this function, we are going to simply list all the processes using the function prototype def process_list(c):
```python

```