# Modules = name.py 
# If other python files (name.py) in your folder contain functions/classes they can be treated as modules.  
# When you import a module the functions/classes are now available for executing in your script. 

import moduleA                  # can be a package or module
import moduleA as mm            # can change the name after importing
from moduleA2 import functionA2 # can import a specific function/class
#from moduleA2 import *         # can import all the functions/classes
import sys

comment = "executing "
print(moduleA.functionA(comment))
print(mm.functionA(comment))
print(functionA2(comment))

print("\n" + __name__ + "is the __name__ of file being executed")
print(moduleA.file_name() + " is the __name__ of the imported file")
print("This is why code inside file's __name__ == '__main__' is only")
print("executed on the file being executed and not when imported.")
#Modules are often designed with the capability to run as a standalone script
#  for purposes of testing the functionality that is contained within the module.
#  This is referred to as unit testing.

print("\nTo see all the functions, properties, methods available in moduleA print out dir()")
print(dir(moduleA))

print("\nThese are 'sys.path' directories python will search to try")
print("and find the modules listed in the 'import' section.")
print("Will include the current directory, $PYTHONPATH, and ")
print("installation dependent default")
# But you can append more locations with sys.path.append('/folder/location/') 
for loc in sys.path:
    print("   " + str(loc))
