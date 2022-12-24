'''
Script : ftp_dictionary
Author : Krishnendu
Purpose : To download file from FTP server
Usage : python ftp_dictionary.py
Revision History :
Aplha Version : 26-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : Here FTP details are declared in a dictionary
'''
# Import modules 
import ftplib

# Variables 
ftp_heanet = {
    "url"  : "ftp.heanet.ie",
    "path" : "/mirrors/ubuntu-cdimage/releases/22.04/release",
    "filename" : "RSA24"
}
# Main code
# Make the connection
ftp = ftplib.FTP(ftp_heanet["url"])
# Anonymous login
ftp.login()
# To list directories
ftp.dir()
# Change current working directory 
ftp.cwd(ftp_heanet["path"])
# FTP file will be downloaded to the current directory
ftp.retrbinary("RETR " + ftp_heanet["filename"], open(ftp_heanet["filename"], 'wb').write)
# To close connection
ftp.quit()