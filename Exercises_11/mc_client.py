'''
Script : tcp_client
Author : Krishnendu
Purpose : Sends multicast packets to a particular address and port.
Usage : python tcp_client.py
Revision History :
Aplha Version : 26-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : The data is sent to a server defined by the settings file, once per second
'''
# Import modules 
import socket 
import time 
from datetime import datetime 
import settings.mc as settings
# Functions 
# Variables 
mc_group = settings.mc_client["mcast_group"]
mc_ip = settings.mc_client["ipv4_address"]
mc_port = settings.mc_client["port"]

# Main code
print(f'This is the client, make sure its IP address matches {mc_ip} in settings.') 
print(f'This selects which interface is used for multicast to {mc_group}.')
print('This script has no error handling, by design')
while True: 
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s: 
# inet_aton converts IPv4 from the a dotted decimal string to 32 bit packed binary format 
        s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(mc_group) + socket.inet_aton(mc_ip)) 
        message_text = f"ATU {datetime.now()}" 
        message = message_text.encode('utf-8') 
        s.sendto(message, (mc_group, mc_port)) 
        print(f'Sent {message_text} to {mc_group}:{mc_port}') 
        time.sleep(1)