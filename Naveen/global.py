#! /usr/bin/python

x=10

def fun():
    global x
    x=20
    print (x)
    x+=10

fun()
print (x)
