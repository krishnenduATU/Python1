'''
Script : udp_client
Author : Krishnendu
Purpose : Send UDP packets to a particular address and port.
Usage : python udp_client.py
Revision History :
Aplha Version : 26-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : The data is sent to a server defined by the settings file, once per second
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
# Main code
print(f'This is the UDP client, it will try to connect to a server at {upd_ip}:{upd_port} in the settings file.') 
print('This script has no error handling, by design')
while True: 
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 
        message_text = f"Sending message {datetime.now()}" 
        message = message_text.encode('utf-8') 
        s.sendto(message, (upd_ip, upd_port)) 
        print(f'Sent {message_text}') 
        time.sleep(1)