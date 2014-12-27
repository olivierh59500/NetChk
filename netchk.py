#!/usr/bin/env python

import netifaces
from netaddr import *
import iptools
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser

a = netifaces.interfaces()

#Look for etho in interface list and proceed if it is
if 'eth0' in a:
	iface = 'eth0'
	addrs = netifaces.ifaddresses(iface)
	#specify AF_INET
	addrs = addrs[netifaces.AF_INET]
	for i in addrs:
		#load IP address
		ip = i['addr']
		#set netmask
		sub = i['netmask']
		#format the cidr string a bit
		cidr = iptools.ipv4.netmask2prefix(sub)
		cidr = str(cidr)
		cidr = "/"+cidr
		#print some output to see what is returned and the network information
		print "IP: ", ip
		print "CIDR: ", cidr
		cmd = ip+"/"+sub
		#get the starting address of the subnet
		rng = iptools.ipv4.subnet2block(cmd)
		startip = rng[0]
		#print rng[0]
		cmd = ip+cidr
		#simple nmap scan to quickly discover assets
		nm = NmapProcess('"'+cmd+'"', options="-sn -n -T5 --open")
		#run the scan
		runscan = nm.run()
		nmap_report = NmapParser.parse(nm.stdout)
		#open file to write results to. Add try and except for some error validation D:
		try:
			out = open('nmap.txt','a')
		except:
			exit("There was an error opening the output file!")
		for scanned_hosts in nmap_report.hosts:
			print scanned_hosts , scanned_hosts.mac
			#write the results. Convert object to string so it doesn't return
			#a buffer error/exception.
			out.write(str(scanned_hosts))
			out.write(str(scanned_hosts.mac))
			out.write("\n")
		out.close()
else:
	exit()