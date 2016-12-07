#!/usr/bin/python
a,b,c,d=10,20,30,40
def funcA():
        a,b,c=100,200,300
        print("In FunA",a,b,c,d)
        def funcB():
                a,b=1000,2000
                print ("In FunctB",a, b, c, d)
                def funcC():
                        a=10000
                        print("In funcC",a,b,c,d)
                funcC()
        funcB()

funcA()

print("In __Main__ ", a,b,c,d)
