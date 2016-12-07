#! /usr/bin/python/
import sys
filename="first.py"
count=0
fileobject=open(filename,"r")
for line in fileobject:
        count+=1
        print("lineNum", count,line,end="")
fileobject.close()

        
