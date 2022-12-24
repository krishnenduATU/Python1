'''
Script : tcp_client
Author : Krishnendu
Purpose : Send TCP packets to a particular address and port.
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
import settings.tcp as settings
# Functions 
# Variables 
tcp_ip = settings.tcp_01["server_tcp_ipv4"]
tcp_port = settings.tcp_01["server_port"]
buffer_size = 1024
# Main code
print(f'This is the TCP client, it will try to connect to a server at {tcp_ip}:{tcp_port} in the settings file.') 
print('This script has no error handling, by design')
while True: 
    print(f'Trying to open a socket to {tcp_ip}:{tcp_port}')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        message_text = f"Sending message {datetime.now()}" 
        message = message_text.encode('utf-8') 
        s.connect((tcp_ip, tcp_port))
        s.send(message) 
        print(f'Sent {message_text} to {tcp_ip}:{tcp_port}') 
        data = s.recv(buffer_size)
        print("Server echoed : ",data)
        time.sleep(1)