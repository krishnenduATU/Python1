'''
Script: convert_temperature.py
By: L00170964
Purpose: To convert temperature in Kelvin to Celsius and Fahrenheit.
Usage : python convert_temperature.py
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 03OCT22
Notes:
Temperatures in Kelvin are stored in list datatype, using list comprehension
convert the kelvin temperature values to Celsius and Fahrenheit. 
'''

print("Program to convert temperature from Kelvin to Celsius & Fahrenheit")
kelvin_list = [33,25,30,20,29,44,45,15,55,273.15]
# Formula to convert Kelvin to Celsius is C = K - 273.15
celsius_list = [f'{(celsius - 273.15) :.2f}' for celsius in kelvin_list]
# Formula to convert Kelvin to Fahrenheit is F = (K − 273.15) × 1.8 + 32
fahrenheit_list = [f'{(((fahrenheit - 273.15 ) * 1.8) + 32):.2f}' for fahrenheit in kelvin_list]
print("Kelvin List : ",kelvin_list)
print("Celsius List : ",celsius_list)
print("Fahrenheit List : ",fahrenheit_list)
print("Using for loop to print list !!")
# To get length of list
len_of_list = len(kelvin_list)
for i in range(len_of_list):
    print(f"{kelvin_list[i]}° Kelvin is same as {celsius_list[i]}° Celsius or {fahrenheit_list[i]}° Fahrenheit")
 