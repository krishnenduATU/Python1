# When all boolean variables were true
boolean_01 = True 
boolean_02 = True 
boolean_03 = True 
if boolean_01: 
    print("boolean_01 was true") 
elif boolean_02: 
    print("boolean_02 was true") 
elif boolean_03: 
    print("boolean_03 was true") 
else: print("None of our boolean variables were true")

# When boolean_01 is false, elif statement is executed
boolean_01 = False 
boolean_02 = True 
boolean_03 = True 
if boolean_01: 
    print("boolean_01 was true") 
elif boolean_02: 
    print("boolean_02 was true") 
elif boolean_03: 
    print("boolean_03 was true") 
else: print("None of our boolean variables were true")

# Code block terminates when first boolean_01 is True
boolean_01 = True 
boolean_02 = False 
boolean_03 = True 
if boolean_01: 
    print("boolean_01 was true") 
elif boolean_02: 
    print("boolean_02 was true") 
elif boolean_03: 
    print("boolean_03 was true") 
else: print("None of our boolean variables were true")

# Code block terminates when first boolean_01 is True
boolean_01 = True 
boolean_02 = True 
boolean_03 = False 
if boolean_01: 
    print("boolean_01 was true") 
elif boolean_02: 
    print("boolean_02 was true") 
elif boolean_03: 
    print("boolean_03 was true") 
else: print("None of our boolean variables were true")

# When all boolean variables were false, else is executed
boolean_01 = False 
boolean_02 = False 
boolean_03 = False 
if boolean_01: 
    print("boolean_01 was true") 
elif boolean_02: 
    print("boolean_02 was true") 
elif boolean_03: 
    print("boolean_03 was true") 
else: print("None of our boolean variables were true")