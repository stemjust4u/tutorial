import os 

comment = "executing "

# PackageD has a __init__.py with the following
'''
__all__ = [
    'moduleD',
    'moduleD2',
]
'''

# So the functions can be called multiple ways

# Full path
#from packageD import *
#import packageD
#print(packageD.moduleD.functionD(comment))
#print(moduleD.functionD(comment))
#print(moduleD2.functionD2(comment))
#print(moduleD3.functionD3(comment))

#print(moduleD2.functionD2(comment))
#print(moduleD3.functionD3(comment)) # will give error since moduleD3 not imported in init.py

# Import a specific module as different name
import packageD.moduleD3 as moduleD3
print(moduleD3.functionD3(comment))

from packageD import *
print(moduleD.functionD(comment))
print(moduleD2.functionD2(comment))
print(moduleD3.functionD3(comment))

from packageD import moduleD
print(moduleD.functionD(comment))
