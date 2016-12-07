#! /usr/bin/python

x,y=10,20


def sum (a,b):

        """print sum of 2 nums
        Hello boy"""
        return a+b


def sum1(a,b,c=0,d=0):
        """ This is a sum of 2, 3, 4 values at a time"""
        print a+b+c+d
        print "a", a,"b", b,"c", c,"d", d


def incr(a,b):
        return (a+1,b+1)

def incr1(a,b):
        a+=1;b+=1
        return(a,b)
#Part5
lst=[10,20]
def incr2(a):
        ctr=0
        while ctr<len(a):
                a[ctr]+=1
                ctr+=1

#Part 5 callby value eg
incr2(lst)
print lst

#part 3(Cal by value)
(x,y)=incr(x,y)
print x,y

#part 4 (Cal by reference)
incr1(x,y)
print x,y

#Part 1
tot=sum(10,20)
print tot
#Part 2
sum1(d=20,a=30,c=50,b=10)
#help(sum)
