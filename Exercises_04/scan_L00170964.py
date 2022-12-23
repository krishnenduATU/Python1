'''
Script: scan_L00170964.py
By: L00170964
Purpose: Script to loop through a dictionary
Prerequisites: Read lecturer note "Walkthroughs - 4. Loops and Statements"
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 01OCT22
Notes:
By default, when using "for" loop to iterate through dictionary keys are returned.
There are methods like values() to return values of a dictionary,
keys() to return keys of a dictionary and items() to return key-value pairs
'''
# Creates a dictionary scan
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}

print("Using scan.keys")
# The keys() method returns keys in dictionary
for ipv4 in scan.keys():
    print(f"IP address for the service : {ipv4}")
print("Using scan.values")
# The values() returns values for keys in dictionary
for port in scan.values():
    print(f"Port number : {port}")
print("Using scan")
# Here loop iterate via keys in dictionary
for ip in scan:
    print(f"IP address : {ip}")
print("Using scan.items")
# Here loop iterate via key-value pair, like shown in tuple unpacking example
for ipv4,port in scan.items():
    print(f"Found a service on IPv4 {ipv4} at port {port}")
