'''
Script : tcp_client
Author : Krishnendu
Purpose : Reads multicast packets from a particular address and port.
Usage : python tcp_client.py
Revision History :
Aplha Version : 26-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes :
'''
# Import modules 
import socket 
import time 
from datetime import datetime 
import settings.mc as settings
# Functions 
# Variables 
mc_group = settings.mc_server["mcast_group"]
mc_ip = settings.mc_server["ipv4_address"]
mc_port = ('', settings.mc_server["port"])

# Main code
print('This is the MC server.')
print(f'This selects which interface is used for multicast to {mc_group}.')
print('This script has no error handling, by design')

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(mc_port)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(mc_group) + socket.inet_aton(mc_ip))
    while True:
        print("Waiting to receive message")
        data,address = s.recvfrom(1024)
        print(f'received {len(data)} bytes from {address}')
        print(data)