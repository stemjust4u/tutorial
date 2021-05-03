import os 

comment = "executing "

# PackageD has a __init__.py with the following
'''
__all__ = [
    'moduleD',
    'functionD'
]
'''
#Both moduleD and functionD are made visible

from packageD import *
print(moduleD.functionD(comment))
#print(moduleD2.functionD2(comment))
#print(moduleD3.functionD3(comment))

from packageD import moduleD
print(functionD(comment))
