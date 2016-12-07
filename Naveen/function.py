#! /usr/bin/python

def sum(a,b,c=0,d=0):
    """print Sum of 4 numbers
    & return sum of 4 nos"""
    #print (a+b)
    return a+b+c+d

c=sum(10,20,30,50)
print (c)
#help(sum)

def sum1(a,b,c=0,d=0):
    print ("a",a," b",b," c",c," d",d)


sum1(b=100,a="Hello",d=20,c=1000)
    


