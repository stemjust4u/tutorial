import sys
import os

newdir = os.path.join(os.path.dirname(__file__), "test1")
os.mkdir(newdir)
print(__name__ + ' creating the dir')

def function_argv2():
    import_dir = os.path.relpath(os.path.abspath(__file__), start=os.curdir)
    comment = "Executing function_argv2 " + import_dir + " functionC"
    return comment


if __name__ == "__main__":
    print('__name__ = ' + str(__name__))
    print('__package__ = ' + str(__package__))    
    print(os.path.dirname(__file__))
    i = 0
    for item in sys.argv:
        print('sys.argv[{0}] = {1}'.format(i, item))
        i += 1