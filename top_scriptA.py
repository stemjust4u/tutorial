# When a module is imported, Python runs all of the code in the module file.
# Since packageA does not have a __init__.py we need to import the full path
# of the modules.
import packageA.moduleA        # full path for the module
from packageA import moduleA2  # slightly different syntax
import sys

comment = "executing "
print(packageA.moduleA.functionA(comment))   # Call the package.module.function
print(packageA.moduleA2.functionA2(comment))

print("\n" + __name__ + "is the __name__ of file being executed")
print(packageA.moduleA.file_name() + " is the __name__ of the imported file")
print("This is why code inside file's __name__ == '__main__' is only")
print("executed on the file being executed and not when imported.")

# You can list the contents of a namespace with dir():
# as you import more objects and assign variables more names are added
print("\nTo see all the functions, properties, methods available in packageA print out dir()")
dir_list = dir(packageA)
dir_list.reverse()
print(dir_list)

print("\nThese are 'sys.path' directories python will search to try")
print("and find the modules listed in the 'import' section.")
print("Will include the current directory, $PYTHONPATH, and ")
print("installation dependent default")
# But you can append more locations with sys.path.append('/folder/location/') 
for loc in sys.path:
    print("   " + str(loc))