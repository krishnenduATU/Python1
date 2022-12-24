'''
Script : tcp_client
Author : Krishnendu
Purpose : Listens for packets on a particular address and port.
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
import settings.tcp as settings
# Functions 
# Variables 
tcp_ip = settings.tcp_01["server_tcp_ipv4"]
tcp_port = settings.tcp_01["server_port"]
buffer_size = 1024
# Main code
print(f'This is the TCP client, it will open port at {tcp_ip}:{tcp_port} and being listening') 
print('This script has no error handling, by design')

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((tcp_ip, tcp_port))
        print(f"Bound to {tcp_ip}:{tcp_port}")
    while True: 
        s.listen(1)
        conn,addr = s.accept()
        print(f'Connection address: {addr}')
        data = conn.recv(buffer_size).decode()
        print(data)
        conn.send(data.encode())
except socket.error as err:
    print("Error raised : ",err)


