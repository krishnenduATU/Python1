# list containing tuples
list_of_tuples = [("SSH",22),("DNS",53),("POP3","110")]
print("Type : ",type(list_of_tuples))
print("List of tuples")
for item in list_of_tuples:
    print(item)
# Unpacking a tuple means dividing its items into independent variables.
print("Example for tuple unpacking") 
for service,port in list_of_tuples:
    print(f"Service {service} is listening to port {port}")

