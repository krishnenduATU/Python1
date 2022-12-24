'''
Script : cpu_log
Author : Krishnendu
Purpose : To create a cpu log within a time interval
Usage : python cpu_log.py
Revision History :
Aplha Version : 26-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : 
'''
# Import modules 
import os, os.path
from time import sleep
import file_utilities
from os_utilities import cpu_load
# Functions 
# Variables 
log_directory = file_utilities.path_name()
filename = file_utilities.log_file_name(".txt")
filepath = log_directory + filename
mode = 0o666
print(log_directory,filename,filepath)
# Main code
# To create the log directory if it doesn't exists
if not os.path.exists(log_directory):
    print(f"Creating directory {log_directory}")
    os.mkdir(log_directory, mode)
else:
    pass

while True:
    sleep(1)
    timestamp = file_utilities.log_file_name("")
    information = cpu_load()
    logline = timestamp + ":" + str(information[0]) + "," + str(information[1]) + "\n"
# creating a file
    try:
        with open(filepath,"a") as file_handle:
            print(f"Writing logs to {filepath}")
            file_handle.write(logline)
    except IOError as err: 
        print(f"IOError was {err}") 
  