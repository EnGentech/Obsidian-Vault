link: [Initial Server Setup with Ubuntu 16.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04)
login to the remote server with 
```terminal
ssh ubuntu@ip_address
```

to check your server configuration, log into the server and type 
```server
cat /etc/ssh/ssh_config
```

On connecting to the server, if you dont have your private key explicitly on the default file location for the private key, then you must define the path when you attempt connection 
```terminal
ssh -i location ubuntu@server_iP
```
To understand how the searches were implemented, use the verbose mode 
```terminal
ssh -i --verbose key_path ubuntu@server_ip
```

## Domain hosting cheap sites
hosting: TmdHosting
Domain: namecheap

use A record to point ip to a domain name if the ip is IPv4, if is is IPv6, then AAA record is used
from domain name to domain name, set up CName record

## Redirection
If a web address changes its path, its needful to redirect users hence not to loose your SEO position
you will need to change the nginx configuration file on your Nginx and use the command below to set the 
1. return 
2. rewrite
syntax applied is 
```nginx
rewrite old_url new_url http-code
```
Note the code varies depending on use
In particular 301 and 307 makes sense
301 is used for permanent redirect
307 is used for temporarily redirect

In this sense the first is used when you have permanently changed your address and the second is used when you probably need to run a maintenance on the server, hence you can move your files to a temporary path and redirect your users using 307 for temporary accessibility e.d
```nginx
rewrite ^/oldpath newpath
```

the redirect can be created in the path 
```nginx
/etc/nginx/sites-enabled/default
```

when you are done with that, restart the server with 

## Restarting server
```nginx
sudo service nginx restart
```

the html directory in nginx is found in 
```nginx
cd /var/www/html
```

link to .tech domain config
```.tech
https://controlpanel.tech/servlet/AuthServlet
```

## Copy files from local machine to server
```terminal
scp /home/username/my/file/to/copy.file derrik@ubuntu-desktop:/home/derrik/Desktop/
```