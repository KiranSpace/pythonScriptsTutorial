#! /usr/bin/python

dow=input("Enter the day of week :")

print (dow.upper())
if (dow.upper() in ("MONDAY" , "TUESDAY" , "WEDNESDAY" , "THURSDAY" , "FRIDAY")):
    print ("9 to 6")

elif (dow.upper() == "SATURDAY"):
    print ("9 to 1")

elif (dow.upper() == "SUNDAY"):
    print ("Holiday")
