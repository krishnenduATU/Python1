'''
Script : cal_endurance
Author : Krishnendu
Purpose : To calculate remaining endurance
Usage : python cal_endurance.py
Revision History :
Aplha Version : 23-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : To calculate remaining endurance in minutes Endurance = Fuel / Fuel Consumption
'''
# Import modules 
# Functions 

def calculate_endurance():
    try:
        fuel = int(input("Fuel value : "))
        fuel_consumption = int(input("Fuel Consumption : "))
        endurance = fuel / fuel_consumption
    except ValueError as err:
        print(f"Enter a integer value, Error : {err}")    
    except ZeroDivisionError as err:
        print(f"Fuel consumption can't be 0, Error : {err}")
    except: # For any other error 
        print(f"General error")
    else: # Code that runs if an error does not occur
        print(f"Endurance = {endurance}")
    finally:
        print("Finished ")
        
# Variables 
# Main code
calculate_endurance()