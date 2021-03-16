# Python is an object oriented programming language (OPP)
# Almost everything in python is an object (ie variables, functions, classes)
# A namespace is a mapping from names to objects.
# Attribute refers to the name after the '.' dot.

# Modules - name.py 
# If other python files (name.py) in your folder contain functions/classes they can be treated as modules.  
# When you import a module python will execute the code in that file
# and the functions/classes are now available for executing in your script. 
# (built-in modules do not have .py, they're written in C and compiled into the python interpreter)

# Package - /folder/
# Starting with Python 3.3 all folders are treated as packages. (Empty __init__.py is not necessary but can add convenience)
# When you import a folder that has a __init__.py file Python will run the code in it. 
import packageB  # importing a package is similar to importing a package.__init__.py file (if it has one)
# Importing a package by itself, that has not init.py, would not be useful
import sys

# Notice the difference from top_scriptA.py. We don't need to include the module since 
# since packageB has a __init__.py that imports the modules
'''
package.B/__init__.py
from .moduleB import *  # import all functions/classes not starting with _ underscore
from .moduleB2 import *
'''
# We can call package.function
comment = "executing "
print(packageB.functionB(comment))  # Since packageB has a __init__.py with module imports inside it
print(packageB.functionB2(comment)) # the module is not required here. Can call package.function
print(packageB.functionB3(comment)) # the module is not required here. Can call package.function


print("\n" + __name__ + "is the __name__ of file being executed")
print(packageB.file_name() + " is the __name__ of the imported file")
print("This is why code inside file's __name__ == '__main__' is only")
print("executed on the file being executed and not when imported.")

print("\nTo see all the functions, properties, methods available in packageB print out dir()")
dir_list = dir(packageB)
dir_list.reverse()
print(dir_list)
print("Note file_name function only listed once although it exists in both modules")
print("Would need to call file_name specifically by module")

print("\nBy moduleB")
dir_list = dir(packageB.moduleB)
dir_list.reverse()
print(dir_list)
print("\nBy moduleB2")
dir_list = dir(packageB.moduleB2)
dir_list.reverse()
print(dir_list)

print("\nCreate BankAccount object")
checking = packageB.BankAccount(200) # INSTANTIATION. Python will run the __init__ method of BankAccount
checking.makeDeposit(100)
checking.makeDeposit(10)
checking.makeWithdrawal(50)
print(checking.getBalance())
print(checking.getDeposits())
print(checking.opendate)
