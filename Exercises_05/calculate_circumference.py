'''
Script: calculate_circumference.py
By: L00170964
Purpose: To calculate circumference of circle with given radius
Prerequisites: Read lecturer note "Walkthroughs - 5. Functions"
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 03OCT22
Notes:
To get radius of circle as a user input of type float and call a function
which return the circumference of circle. 
'''
def calculate_circumference(radius):
    # circumference of circle is 2* pie *radius, 2f means rouding to 2 float digits
    circumference = f'{(2 * 3.142 * radius) :.2f}'
    return circumference
# Takes input in float type, default value is set to 1
radius_of_circle = float(input("Enter radius of circle : ")or 1)
# Call function and store return value
circumference_of_circle = calculate_circumference(radius_of_circle)
print(f'Circumference of circle with radius {radius_of_circle} = {circumference_of_circle}')