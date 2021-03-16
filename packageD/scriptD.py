import sys, os 

print(sys.path[0])

from moduleD import functionD    # moduleD's are in same directory
from moduleD3 import functionD3


comment = "executing "
print("\n" + functionD(comment))

comment = "executing "
print("\n" + functionD3(comment))
