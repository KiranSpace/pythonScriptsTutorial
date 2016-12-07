#! /usr/bin/python

import sys


dir(sys)
sys.setrecursionlimit(2147483647)

x,y=10,20
def incr(a,b):
    a+=1;b+=1
    return(a,b)
    print (a,b)

incr(x,y)
print(x,y)


lst=[10,20]
def incr1(a):
    ctr=0
    while ctr<len(a):
        a[ctr]+=1
        ctr+=1

incr1(lst)
print(lst)

seq=(10,20)
print(id(seq))
def incr1(a):
    ctr=0;print (id(a))
    while ctr<len(a):
        break
        #a[ctr]+=1
        #ctr+=1

incr1(seq)
print(seq)


def factorial(n):
    if (n < 0):
        print("Error! Factorial of a negative number doesn't exist.");

    else:
        if (n >= 1):
            return n*factorial(n-1)
        else:
            return 1
        
a=int(input("enter the positive number to find factorial:"))    
fact=factorial(a)
print ("The factorial of", a , "is :", fact)


