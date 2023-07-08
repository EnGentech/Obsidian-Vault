link: https://www.youtube.com/watch?v=Ay8jOdu3nK8
## Configuration 
first install the file using 
```haproxy
sudo apt-get install --no-install-recommends software-properties-common
add-apt-repository ppa:vbernat/haproxy-2.0
apt-get install haproxy=2.0./**
```

after installation, go into the config file
using the path
```path
/etc/haproxy/haproxy.cfg
```

## Code for checks
check if the severs are active
```haproxy
netstat -ntalp | grep 80
```
check for logs if issues arises
```haproxy
tail -f /var/log/messages
```

## link: [How to Set Up an HAProxy Load Balancer (howtogeek.com)](https://www.howtogeek.com/devops/how-to-set-up-an-haproxy-load-balancer-and-why-youd-want-to/)