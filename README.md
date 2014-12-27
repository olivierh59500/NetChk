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

`pip install requests`


**OUTPUT**
```
root@kali:~/py# ./netchk.py 
IP:  192.168.0.71
CIDR:  /24
NmapHost: [192.168.0.1 () - up] 00:14
NmapHost: [192.168.0.3 () - up] 5C:DA
NmapHost: [192.168.0.21 () - up] 28:18
NmapHost: [192.168.0.54 () - up] D0:E7
NmapHost: [192.168.0.56 () - up] FC:C2
NmapHost: [192.168.0.60 () - up] 78:1C
NmapHost: [192.168.0.65 () - up] D0:E7
NmapHost: [192.168.0.73 () - up] 30:F9
NmapHost: [192.168.0.74 () - up] 00:90
NmapHost: [192.168.0.75 () - up] 00:16
NmapHost: [192.168.0.76 () - up] 40:F0
NmapHost: [192.168.0.78 () - up] 28:18
NmapHost: [192.168.0.82 () - up] EC:E0
NmapHost: [192.168.0.86 () - up] 68:A8
NmapHost: [192.168.0.98 () - up] B0:E8
NmapHost: [192.168.0.134 () - up] D8:EB
NmapHost: [192.168.0.71 () - up] 
Check HW vendor? (y/n): y




NmapHost: [192.168.0.1 () - up]00:14
Dell Inc 

NmapHost: [192.168.0.3 () - up]5C:DA
Murata Manufacturing Co., Ltd. 

NmapHost: [192.168.0.21 () - up]28:18
Microsoft Corporation 

NmapHost: [192.168.0.54 () - up]D0:E7:82
```
