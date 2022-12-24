'''
Script : ftp_file_downloader
Author : Krishnendu
Purpose : To download file from FTP server
Usage : python ftp_file_downloader.py
Revision History :
Aplha Version : 26-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : FTP details are added in ./settings directory. 
'''
# Import modules 
import ftplib
import settings.ftp_clients as settings
# Functions 
# Variables 
# Main code
# Make the connection
ftp = ftplib.FTP(settings.ftp_heanet["url"])
# Anonymous login
ftp.login()
ftp.dir()
# Change current working directory 
ftp.cwd(settings.ftp_heanet["path"])
# FTP file will be downloaded to the current directory
ftp.retrbinary("RETR " + settings.ftp_heanet["filename"], open(settings.ftp_heanet["filename"], 'wb').write)
# To close connection
ftp.quit()