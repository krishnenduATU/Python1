'''
Script : file_operations
Author : Krishnendu VP
Purpose : To perform basic operations on a file
Usage : python file_operations.py
Revision History :
Aplha Version : 23-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : Walkthroughs - 7. Handling Errors
'''
# Import modules 
import os, platform

# Variables 
filename = "logfile.txt"
current_working_directory = os.getcwd()
# Main code
try:
# a : append ; w : write ; r : read ; rw : read & write 
    with open(filename,"a") as file_handle:
        print(f"Appending lines to file {current_working_directory}\{filename}")
        file_handle.write("Test line ...")
except IOError as err: 
    print(f"IOError was {err}") 
except EOFError as err: 
    print(f"End of file error was {err}") 
except OSError: 
    print("OS Error") 
except:
    print("General Error ..")
else: 
    print("File created") 
finally: 
    print("Finishing up!") 
# close not needed because with statement 
# # file_handle.close()