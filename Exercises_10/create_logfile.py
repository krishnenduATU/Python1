'''
Script : create_logfile
Author : Krishnendu
Purpose : To create a logfile name and path based on OS used
Usage : python create_logfile.py
Revision History :
Aplha Version : 26-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : This script calls file_utilities.py and os_utilities.py
'''
# Import modules 
'''
Note : OS detection is also used in file_utilities, so this program will work
if we import file_utilities alone too 
'''
from file_utilities import path_name, log_file_name 
from os_utilities import detect_os
# Main code
this_os = detect_os() 
log_path = path_name() 
filename = log_file_name(".log") 
print(f"File path on {this_os} OS : {log_path}{filename}" )