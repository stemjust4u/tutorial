# __init__.py will be used when the package/folder is imported
# the '.' dot indicates importing from current directory
from .moduleB import *  # import all functions/classes not starting with _ underscore
from .moduleB2 import *

# Using * is convenient but not recommended. Both modules have a function called file_name that the user
# would need to know before calling it in top_scriptB.py
