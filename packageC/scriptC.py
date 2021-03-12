import sys, os 
print("Since scriptC is inside packageC folder and not at the top it does not have immediate access to")
print("packageA/B modules. ")
print(sys.path[0])

print("\nBut you can append more locations, further up the dir tree, with sys.path.append('/folder/location/')")
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_path)
print(sys.path[-1:])  # see the last path added from sys.path.append

from packageA import moduleA  
print("With the top directory /tutorial/ added we can now import packageA.moduleA")

comment = "ScriptC can now execute a function in a different directory.. "
print("\n" + moduleA.functionA(comment))

import packageB     # packageB has __init__.py that imports the modules for us
print("\n" + packageB.functionB(comment)) # do not have to list the module
