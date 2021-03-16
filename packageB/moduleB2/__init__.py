# moduleB2 is a subpackage
# Can control which functions are available by adding/removing in __all__
# Could remove functionB3 so it doesn't show up in pydoc
# But could still access 

from .funcb2imp import *
from .funcb3imp import *

__all__ = ['functionB2', 'functionB3']