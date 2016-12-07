#! /usr/bin/python

import getpass

username=input("Username :")
password=getpass.getpass("password :")

if(username == "Naveen") and (password == "Naveen"):
        print("login successfull")
else:
        print("login un-successfull")
        
