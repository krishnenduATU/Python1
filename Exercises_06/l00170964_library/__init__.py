# Packages are collection of modules.
'''
.square_module points to Exercises_06\l00170964_library\square_module.py
Below line imports all function inside square_module.py, to import only one function
use "from .square_module import square_number"
'''
from .square_module import *
from .cube_module import *
# Defining global variable in __init__.py 
copyright = "© Krish 2022"