# Using for loop to populate a list
list_01 = []
string = "Morning Folks!"
for letter in string:
    list_01.append(letter)
print("Appending list using for loop : ",list_01)

# Using List comprehension to append values to list
list_comprehension = [letter for letter in string ]
print("Appending list using list comprehension : ",list_comprehension)

# To print numbers from 1-10 using list comprehension
number_list = [num for num in range(1,10)]
print("Using List comprehension to print numbers in a range : ", number_list)

# To perform operations on variables
number_list = [num * 10 for num in range(1,10)]
print("Using List comprehension for arthematic operations : ",number_list)

# List comprehension and if statement
number_list = [num for num in range(1,10) if num < 5]
print("List comprehension with if statement", number_list)

# Feet to meters conversion, 1 feet = 0.3048 meters
conversion = 0.3048
values_in_feet = [12.3, 13.8, 15.3, 12.1, 8.8]
# f string is used to round off the values to 2 floating digits
values_in_meters = [f'{(num * conversion):.2f}' for num in values_in_feet]
print("Values in feet : ",values_in_feet)
print("Values in meters : ",values_in_meters)
