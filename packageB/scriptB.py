# Modules = name.py 
# If other python files (name.py) in your folder contain functions/classes they can be treated as modules.  
# When you import a module the functions/classes are now available for executing in your script. 

import moduleB                  # can be a package or module
from moduleB2 import functionB2 # can import a specific function/class
import sys

comment = "executing "
print(moduleB.functionB(comment))
print(functionB2(comment))

print("\n" + __name__ + "is the __name__ of file being executed")
print(moduleB.file_name() + " is the __name__ of the imported file")
print("This is why code inside file's __name__ == '__main__' is only")
print("executed on the file being executed and not when imported.")

print("\nTo see all the functions, properties, methods available in moduleB print out dir()")
print(dir(moduleB))

print("\nThese are 'sys.path' directories python will search to try")
print("and find the modules listed in the 'import' section.")
print("Will include the current directory, $PYTHONPATH, and ")
print("installation dependent default")
# But you can append more locations with sys.path.append('/folder/location/') 
for loc in sys.path:
    print("   " + str(loc))
