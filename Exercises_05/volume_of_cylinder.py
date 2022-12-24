'''
Script: volume_of_cylinder.py
By: L00170964
Purpose: To calculate volume of cylinder
Usage : python volume_of_cylinder.py
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 04OCT22
Notes:
To calculate volume of cylinder with a given height and radius from 
user input. Instead of functions, lambda is used here. ValueError exception
is handled, incase if user inputs any other character other than int/float.
'''
# Function to print usage of script if it throws an error
def help():
    print("Usage: python volume_of_cylinder.py \nHeight & radius accepts integers/floating numbers only")

print("Program to calculate volume of a cylinder")
user_input = ''
while user_input is not float:
    try:
        # Handling Exceptions, if users enter a value other than int/float
        height = float(input("Enter height of the cylinder : ") )
        radius = float(input("Enter radius of the cylinder : ") )
        break
    except ValueError:
        help()

# Volume of cylinder = Pie * radius * radius * height 
volume = lambda height, radius : 3.142 * radius * radius * height
print(f"Volume of cylinder of height {height} and radius {radius} is {(volume(height, radius)):.2f}")