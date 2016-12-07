#! /usr/bin/python

import sys
sys.setrecursionlimit(2147483647)
def fact(num):
        if num>=1:
                 return num*fact(num-1)
        return 1

value=fact(999)
print value

print sys.getrecursionlimit()
