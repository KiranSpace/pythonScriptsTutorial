#! /usr/bin/python

import sys
count=0
fileobject=open('dow.py','r')
for line in fileobject:
        count+=1;
#        line=fileobject.readline()
        print (count," ", line,end="")
        
fileobject.close()


