[If you are having trouble restarting the Nginx server, you can try the following solutions](https://www.bing.com/ck/a?!&&p=dd0ccea105b35bfeJmltdHM9MTY4ODQyODgwMCZpZ3VpZD0wZTc4MjQ3Mi1iNWE4LTY0ZTEtMjM4YS0zNjk0YjRiNTY1MTUmaW5zaWQ9NTYzMA&ptn=3&hsh=3&fclid=0e782472-b5a8-64e1-238a-3694b4b56515&psq=nginx+could+not+restart+because+it+encountered+error+solution&u=a1aHR0cHM6Ly93d3cubWlsZXN3ZWIuY29tL2hvc3RpbmctZmFxcy9zZXJ2aWNlLW5naW54LXJlc3RhcnQtZmFpbHMv&ntb=1)[1](https://www.bing.com/ck/a?!&&p=4288d4bdd0f2d0d1JmltdHM9MTY4ODQyODgwMCZpZ3VpZD0wZTc4MjQ3Mi1iNWE4LTY0ZTEtMjM4YS0zNjk0YjRiNTY1MTUmaW5zaWQ9NTYzMQ&ptn=3&hsh=3&fclid=0e782472-b5a8-64e1-238a-3694b4b56515&psq=nginx+could+not+restart+because+it+encountered+error+solution&u=a1aHR0cHM6Ly93d3cubWlsZXN3ZWIuY29tL2hvc3RpbmctZmFxcy9zZXJ2aWNlLW5naW54LXJlc3RhcnQtZmFpbHMv&ntb=1)[2](https://www.bing.com/ck/a?!&&p=daf483f4aed9c39fJmltdHM9MTY4ODQyODgwMCZpZ3VpZD0wZTc4MjQ3Mi1iNWE4LTY0ZTEtMjM4YS0zNjk0YjRiNTY1MTUmaW5zaWQ9NTYzMg&ptn=3&hsh=3&fclid=0e782472-b5a8-64e1-238a-3694b4b56515&psq=nginx+could+not+restart+because+it+encountered+error+solution&u=a1aHR0cHM6Ly9zdGFja292ZXJmbG93LmNvbS9xdWVzdGlvbnMvNTk3NzY3NzMvY2FudC1yZXN0YXJ0LW5naW54LXdlYi1zZXJ2ZXI&ntb=1)[3](https://www.bing.com/ck/a?!&&p=764a2ad41076dc3dJmltdHM9MTY4ODQyODgwMCZpZ3VpZD0wZTc4MjQ3Mi1iNWE4LTY0ZTEtMjM4YS0zNjk0YjRiNTY1MTUmaW5zaWQ9NTYzMw&ptn=3&hsh=3&fclid=0e782472-b5a8-64e1-238a-3694b4b56515&psq=nginx+could+not+restart+because+it+encountered+error+solution&u=a1aHR0cHM6Ly9zdGFja292ZXJmbG93LmNvbS9xdWVzdGlvbnMvNDAyOTI0MjAvd2h5LWRvZXMtbmdpbngtZmFpbC10by1zdGFydA&ntb=1):

- Run the command "sudo nginx -t" to find any errors in the config file.
- If there are no errors, execute the command "sudo service nginx reload".
- Check the error log to find the issue.
- Check if there is no Nginx process running, and kill it if there is.
- Write the ID number of the process to the /run/nginx.pid file.

## Nginx default configuration file
```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    # SSL configuration
    #
    # listen 443 ssl default_server;
    # listen [::]:443 ssl default_server;
    #
    # Note: You should disable gzip for SSL traffic.
    # See: https://bugs.debian.org/773332
    #
    # Read up on ssl_ciphers to ensure a secure configuration.
    # See: https://bugs.debian.org/765782
    #
    # Self signed certs generated by the ssl-cert package
    # Don't use them in a production server!
    #
    # include snippets/snakeoil.conf;

    root /var/www/html;

    # Add index.php to the list if you are using PHP
    index index.php index.html index.htm index.nginx-debian.html;

    server_name x.x.x.x;

    location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        try_files $uri $uri/ =404;
    }

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #


/* additions i made*/


    error_page 404 /404.html;
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
    root /usr/share/nginx/html;
    }
    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        try_files $uri = 404;
        fastcgi_split_path_info ^(.*\.php)(/.*)$;
        
        # With php7.0-cgi alone:
    #   fastcgi_pass 127.0.0.1:9000;
    #   # With php7.0-fpm:
        fastcgi_pass unix:/run/php/php7.0-fpm.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root $fastcgi_script_name;
        include fastcgi_params;
    }

/*end of additions*/



    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #   deny all;
    #}
}


# Virtual Host configuration for example.com
#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
#server {
#   listen 80;
#   listen [::]:80;
#
#   server_name example.com;
#
#   root /var/www/example.com;
#   index index.html;
#
#   location / {
#       try_files $uri $uri/ =404;
#   }
#}
```