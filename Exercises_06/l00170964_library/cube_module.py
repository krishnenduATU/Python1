# Function to print cube of given number
def cube_number(num):
    return num * num * num

# __name__ will return value “__main__” if the script is executed as main program else the module's name
def cube_text():
    print(f"This module is called {__name__}. Printing from function square_text")

# To use functions when executed as standalone script
if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script") 
    input_num = int(input("Enter a number : "))
    print(f"Cube of {input_num} = {cube_number(input_num)}")
else:
    print(f"This module is called {__name__} and is being called by another script")



