'''
Script : udp_client
Author : Krishnendu
Purpose : Listens for packets on a particular address and port.
Usage : python udp_client.py
Revision History :
Aplha Version : 26-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : The data sent from the udp_client.py is read
'''
# Import modules 
import socket 
import time 
from datetime import datetime 
import settings.udp_clients as settings
# Functions 
# Variables 
upd_ip = settings.udp_client_01["server_udp_ipv4"]
upd_port = settings.udp_client_01["server_port"]
buffer_size = 1024
# Main code
print(f'This is the UDP server, it will open port at {upd_ip}:{upd_port} and being listening') 
print('This script has no error handling, by design')

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 
    s.bind((upd_ip,upd_port)) 
    print(f'Listening on  {upd_ip}') 
    while True:
        data,addr = s.recvfrom(buffer_size)
        data = data.decode()
        print(addr,data)