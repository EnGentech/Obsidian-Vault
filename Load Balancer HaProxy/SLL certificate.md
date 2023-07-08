To terminate SSL on HAproxy means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination. To create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www., you must ensure that HAproxy is listening on port TCP 443 and accepting SSL traffic. You must also ensure that HAproxy serves encrypted traffic that will return the / of your web server. When querying the root of your domain name, the page returned must contain Holberton School.

Here is an example of how to configure SSL termination on HAProxy on Ubuntu 22.041:

Install certbot by running the following command:
sudo apt install certbot

Create a directory where all the files will be placed:
sudo mkdir -p /etc/haproxy/certs

Generate a certificate using certbot:
sudo certbot certonly --standalone -d www.example.com -d example.com -m admin@example.com --agree-tos

Combine the fullchain.pem and privkey.pem file into one file:
sudo cat /etc/letsencrypt/live/www.example.com/fullchain.pem /etc/letsencrypt/live/www.example.com/privkey.pem | sudo tee /etc/haproxy/certs/example.pem

Configure HAProxy to accept encrypted traffic for your subdomain www. by adding the following lines to your haproxy.cfg file:
frontend www-https
    bind *:443 ssl crt /etc/haproxy/certs/example.pem
    mode http
    default_backend www-backend

backend www-backend
    mode http
    balance roundrobin
    server web1 192.168.1.10:80 check

Restart HAProxy:
sudo systemctl restart haproxy.service

