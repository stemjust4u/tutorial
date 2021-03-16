import sys
import os.path
from pathlib import Path

testdir = os.path.join(os.path.dirname(__file__), "test1")
Path(os.path.join(testdir, 'testfile.txt')).touch()
testfile = os.path.join(testdir, 'testfile.txt')
print(__name__ + ' reading the testfile.txt')

with open(testfile, "r") as f:
    fcontent = "content of the file: " + f.read()

print(fcontent)

if __name__ == "__main__":
    print('__name__ = ' + str(__name__))
    print('__package__ = ' + str(__package__))    
    os.path.dirname(__file__)
    i = 0
    for item in sys.argv:
        print('sys.argv[{0}] = {1}'.format(i, item))
        i += 1