'''
Script : file_utilities
Author : Krishnendu
Purpose :  To return file path based on OS, filename (with timestamp) 
Usage : python file_utilities.py
Revision History :
Aplha Version : 25-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : 
'''
# Import modules
from datetime import datetime as dt 
import sys, csv

# Functions 
def path_name():
    this_os = sys.platform
    if this_os == "win32":
        return "C:/logfiles/"
    elif this_os == "linux":
        return '/home/pi/logfiles/'
    else:
        print(f'Unsupported OS: {this_os}')
        exit(0)

def log_file_name(extension):
    """ 
    Create a file name in the logfiles directory, based on current data and 
    time. Requires the computer to have an RTC or synched clock 
    """ 
    now = dt.now()
    file_name = '%0.4d%0.2d%0.2d-%0.2d%0.2d%0.2d' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
    return file_name + extension
    
# Main code
if (__name__ == '__main__'): 
    print(f"This module is called {__name__} and executes as a standalone script") 
    log_path = path_name() 
    filename = log_file_name(".log") # Create a file like logfiles "20221026-160112.log"
    print(log_path + filename )
else:
    pass
    #print(f"This module is called {__name__} and is being called by another script")

