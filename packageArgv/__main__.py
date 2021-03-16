# To directly execute a package from command line. ie $ python3 -m packageArgv
# package needs to have a __main__.py

import sys
import os.path

if __name__ == "__main__":
    print('__name__ = ' + str(__name__))
    print('__package__ = ' + str(__package__))    
    os.path.dirname(__file__)
    i = 0
    for item in sys.argv:
        print('sys.argv[{0}] = {1}'.format(i, item))
        i += 1