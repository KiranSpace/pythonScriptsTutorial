#! /usr/bin/python
#Script to print prime numbers from 1 to 100 using while

# Python program to display all the prime numbers within an interval

# change the values of lower and upper for a different result
lower = 2
upper = 100

# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

while lower<upper:
    if lower>1:
        num=2
        while num<lower:
            num+=1
            if (lower % (num-1)) == 0:
                break
        else:
           print(lower)
    lower+=1       
