
# To illustrate an example of item iteration in a "for" loop.
iterable_variable = [1,2,3,4,5,6] 
print("Print items in list using for loop")
for item in iterable_variable: 
    # For each item, execute this code block print(item)
    print(item)

# loop to print odd numbers in the list
print("Odd numbers in list are : " , end =" ")
for item in iterable_variable: 
    if item %2 != 0: 
        print(item,end=" ")

# loop to print even numbers in the list
print("\nEven numbers in list are : " , end =" ")
for item in iterable_variable: 
    if item %2 == 0: 
        print(item,end=" ")

# To add each number in the list
total = 0
for item in iterable_variable:
    total = total + item
# if print is in same indent as of "total", it will print message 6 times 
print("\nSum of items in list = ",total) 

# Range(start, stop, step)
print("Printing numbers from 0-100 with step 10")
for number in range(0,100,10):
    print(number)