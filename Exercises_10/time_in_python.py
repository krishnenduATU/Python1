'''
Script : time_in_python
Author : Krishnendu
Purpose : Using Python to handle time
Usage : python time_in_python.py
Revision History :
Aplha Version : 25-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : To print human readable values for current time
'''
# Import modules 
from datetime import datetime as dt
# Variables 
date_format = "%d/%m/%Y"
current_date_with_time = dt.now()
current_date = dt.now().strftime("%c")
current_year = dt.now().strftime("%Y or %y ") # 
current_month = dt.now().strftime("%B or %b or %m") # B > Month in words, m > Month in number format
current_day = dt.now().strftime("%A or %d")
current_time_24 = dt.now().strftime("%H:%M:%S")
current_time_12 = dt.now().strftime("%I:%M:%S")
  
# Main code
print("Current date with time : ",current_date_with_time)
print("Current date : ",current_date)
print("Current time in 24hr format : ",current_time_24)
print("Current time in 12hr format : ",current_time_12)
print("Current year : ",current_year)
print("Current month : ",current_month)
print("Current day : ",current_day)
print("Current date in dd/mm/yyyy : ",dt.now().strftime("%d/%m/%Y"))
print("Current time in dd-month-yy : ",dt.now().strftime("%d-%b-%y"))

# Program to calculate days between two dates
from_date = str(input("Enter FROM date in dd/mm/yyyy: "))
to_date = str(input("Enter TO date in dd/mm/yyyy: "))
from_date = dt.strptime(from_date, date_format)
to_date = dt.strptime(to_date, date_format)
total_days = to_date - from_date
print(f"No: of days = {total_days.days}")