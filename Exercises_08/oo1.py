'''
Script : oo1
Author : Krishnendu
Purpose : To demostrate anatomy of a simple class
Usage : python oo1.py
Revision History :
Aplha Version : 25-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : Anatomy of a simple class
'''
class KrishClass():
    '''This is a doc string for new class'''
    college_id = "170964"
    def __init__(self, my_greeting): 
        print("Running constructor for KrishClass") 
        # Create attributes and set initial values 
        self.message = my_greeting 
    def my_method(self): 
        print(self.message) 
# New object instance of KrishClass
my_class1 = KrishClass("Morning Krish!") 
my_class1.my_method() 
my_class2 = KrishClass("ID")
#print(type(my_class1))

print(my_class2.college_id) 
print("Doc String : ",KrishClass.__doc__) # To print doc string
