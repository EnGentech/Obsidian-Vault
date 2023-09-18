link: [How To Create a Self-Signed SSL Certificate for Nginx in Ubuntu 20.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-20-04-1)

or 

follow the guide:
1. Install Certbot:
First, ensure you have Certbot installed on your server. The method varies depending on your operating system. Here are the commands for some common Linux distributions:
For Ubuntu/Debian:
sudo apt-get update
sudo apt-get install certbot python3-certbot-nginx

For CentOS/RHEL:
sudo yum install certbot python3-certbot-nginx

2. Obtain an SSL Certificate:
Run Certbot to obtain an SSL certificate for your domain. Replace example.com with your domain name.
sudo certbot --nginx -d example.com -d www.example.com

Certbot will prompt you to provide an email address for renewal reminders and agree to the terms of service. After that, it will automatically configure Nginx to use the SSL certificate.
3. Configure Nginx to Redirect HTTP to HTTPS:
Certbot should have already configured Nginx to use SSL. Now, you'll need to configure Nginx to redirect all HTTP traffic to HTTPS.
Open your Nginx configuration file for your site. This file is often located in /etc/nginx/sites-available/ or /etc/nginx/conf.d/. Replace your-site.conf with your actual site's configuration file name:
sudo nano /etc/nginx/sites-available/your-site.conf

Inside the server block, add a new server block to handle HTTP requests and redirect them to HTTPS. It should look something like this:

server {
    listen 80;
    server_name example.com www.example.com;

    location / {
        return 301 https://$host$request_uri;
    }
}

Save the file and exit the text editor.
4. Test Nginx Configuration:
Before applying the changes, it's a good practice to test the Nginx configuration to ensure there are no syntax errors:
sudo nginx -t

If there are no errors, you should see a message like "syntax is okay" and "test is successful."
5. Reload Nginx:
Now, reload Nginx to apply the configuration changes:

sudo systemctl reload nginx

6. Automatic Renewal:
Let's Encrypt certificates expire after 90 days, so it's essential to set up automatic renewal. Certbot should have already created a systemd timer to handle this, but you can check it with:

sudo systemctl list-timers | grep certbot

You should see a timer for Certbot's renewal. Certbot will automatically attempt to renew your certificate when it's about to expire.
That's it! Your Nginx server should now be configured to redirect all HTTP traffic to HTTPS, and your SSL certificate should automatically renew when necessary.