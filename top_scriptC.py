comment = "executing "

# PackageC has a __init__.py with the following
'''
import packageC.moduleC
import packageC.moduleC2
import packageC.moduleC3
'''

# So the functions can be called multiple ways

# Full path
import packageC 
print(packageC.moduleC.functionC(comment))
print(packageC.moduleC2.functionC2(comment))
print(packageC.moduleC3.functionC3(comment))

# Import a specific module
from packageC import moduleC2
print(moduleC2.functionC2(comment))
# Import a specific module as different name
import packageC.moduleC3 as mm3
print(mm3.functionC3(comment))
