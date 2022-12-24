'''
Script : devices
Author : Krishnendu
Purpose : A basic class model to build network automation code and utilities.
Usage : python devices.py
Revision History :
Aplha Version : 25-Oct-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : Walkthroughs - 8. OO Coding here
'''
""" 
Parent class Template by JOR 
""" 
# In any complex application, create a base class which will never be instantiated. 
class Device(): 
# Define a class object attribute, it will be the same for any instance of the class 
    pi = 3.142 
# Constructor, called whenever an instance of the class is created. 
def __init__(self) -> None: 
    print("Running constructor for base class") 
# Create attributes and set initial values 
    self.debug = False 
def run(self): 
    raise NotImplementedError("This is an abstract class, do not instantiate") 
def calculate_crc(self, frame:str)->int: 
    print("Checking CRC from base") 
# Put real code in here, this is a dummy value for initial setup 
    crc = 123456789 
    return crc 
""" 
Child class Template : Firewall 
""" 
# Create child class which can access the methods and properties of the base class 
class Firewall(Device): 
# Constructor, called whenever an instance of the class is created. 
# Use parameter1 as a tag to identify the object 
    def __init__(self, parameter1) -> None: 
# Call back to the parent class 
        Device.__init__(self) 
        print(f"Running constructor for {parameter1}") 
# Create attributes and set initial values 
        self.parameter1 = parameter1 
        self.test_message = "" 
    def configure_firewall(self): 
        print("Configuring Firewall") 
    def calculate_crc(self, frame:str)->int: 
        pi_value = Device()
        print(pi_value.pi)
        print("Checking CRC from child") 
# Put real code in here, this is a dummy value for initial setup 
        crc = 123456789 
        return crc 
""" 
Child class Template : Switch 
""" 
# Create child class which can access the methods and properties of the base class 
class Switch(Device): 
# Constructor, called whenever an instance of the class is created. 
# Use parameter1 as a tag to identify the object 
    def __init__(self, parameter1) -> None: 
# Call back to the parent class 
        Device.__init__(self) 
        print(f"Running constructor for {parameter1}") 
# Create attributes and set initial values 
        self.parameter1 = parameter1 
        self.test_message = "" 
    def configure_switch(self): 
        print("Configuring Switch") 
    def calculate_bandwidth(self, frame:str)->int: 
        print("Checking Switch bandwidth") 
# Put real code in here, this is a dummy value for initial setup 
        bandwidth = 123456789 
        return bandwidth 

""" 
Child class Template : LoadBalancers
""" 
# Create child class which can access the methods and properties of the base class 
class LoadBalancers(Device): 
# Use parameter1 as a tag to identify the object 
    def __init__(self, parameter1) -> None: 
# Call back to the parent class 
        Device.__init__(self) 
        print(f"Running constructor for {parameter1}") 
# Create attributes and set initial values 
        self.parameter1 = parameter1 
        self.test_message = "" 
    def configure_loadbalancer(self): 
        print("Configuring LoadBlancer") 
    def get_domain_name(self)->str: 
        print("Checking balancers domain name") 
# Put real code in here, this is a dummy value for initial setup 
        domain_name = "cisco.route.loadblancer.com" 
        return domain_name 