'''
Script : class_template
Author : Krishnendu
Purpose : To create a template for a simple class
Usage : python class_template.py
Revision History :
Aplha Version : 30-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : A simple class template that can be reused in other programs too
'''
# Class 
class DummyClass():
    # Constructor, called whenever an instance of the class is created.
    # Passing the self keyword to connect this method to the instance of the class.
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor ran") 
        # Adding attributes to a class
        self.class_object_attribute1 = attribute1
        self.class_object_attribute2 = attribute2
    # Default Methods
    def dummy_method(self):
        if self.class_object_attribute2:
            print(f"Hello {self.class_object_attribute1}, Good morning !!")
        else:
            print(f"Hello {self.class_object_attribute1}, hmmm !!")
    # Pass an argument to a method
    def dummy_arg_method(self,arg1:str):
        print(f"Hello {arg1}")
# To instantiate an object
dummy_object = DummyClass("Krish", True)

# Main code
# Check the object type
print(type(dummy_object))

print(f"Object Attribute 1 : {dummy_object.class_object_attribute1}")
print(f"Object Attribute 2 : {dummy_object.class_object_attribute2}")
# To call method
dummy_object.dummy_method()
# To pass argument to method
dummy_object.dummy_arg_method("Krish")