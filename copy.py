#! /usr/bin/python/
import sys
filename1="first.py"
filename2="sample.py"
count=0
fileobject1=open(filename1,"r")
fileobject2=open(filename2,"w")
for line in fileobject1:
        count+=1
        fileobject2.write(line)
        print("lineNum", count,line,end="")
fileobject1.close()
fileobject2.close()
