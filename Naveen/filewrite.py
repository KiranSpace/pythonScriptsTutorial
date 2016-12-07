#! /usr/bin/python

import sys

fileobjectread=open('dow.py','r')
fileobjectwrite=open('manju.py','w')

for line in fileobjectread:
        fileobjectwrite.write(line)
        
fileobjectread.close()
fileobjectwrite.close()

