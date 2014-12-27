NetChk
======

**Please note that this is for a project that I am working on. Expect many errors and constant changes if you decide to mess with this**

Python script to quickly scan and profile joined network. 

This script can also determine the vendor of a MAC address through public API using the requests library 

Dependencies:
netifaces
netaddr
iptools
libnmap
requests

You can install these dependencies using pip:

`pip install netifaces`

`pip install netaddr`

`pip install iptools`

`pip install python-libnmap`

```
root@kali:~/py# ./netchk.py 
IP:  192.168.0.71
CIDR:  /24
NmapHost: [192.168.0.1 () - up]
NmapHost: [192.168.0.3 () - up]
NmapHost: [192.168.0.21 () - up]
NmapHost: [192.168.0.54 () - up]
NmapHost: [192.168.0.56 () - up]
NmapHost: [192.168.0.60 () - up]
NmapHost: [192.168.0.65 () - up]
NmapHost: [192.168.0.73 () - up]
NmapHost: [192.168.0.74 () - up]
NmapHost: [192.168.0.75 () - up]
NmapHost: [192.168.0.76 () - up]
NmapHost: [192.168.0.78 () - up]
NmapHost: [192.168.0.82 () - up]
NmapHost: [192.168.0.86 () - up]
NmapHost: [192.168.0.98 () - up]
NmapHost: [192.168.0.134 () - up]
NmapHost: [192.168.0.71 () - up]
```
