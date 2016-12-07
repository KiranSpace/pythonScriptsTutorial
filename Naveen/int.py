#! /usr/bin/python

#help(int)
#print(dir(int))

class date():
    def __init__(self, d = 0, m = 0, y = 0):
        self.d = d
        self.m = m
        self.y = y
    
    def __add__(self,other):
        self.d+=(self.d%30)
        
        if(self.d%30!=0) and (self.m<12):
            self.m+=int(self.d/30)
            if(self.m>12):
                self.m=int(self.m/12)
            self.d=int(self.d%30)            
        else:
            self.m
            
        if(self.m>12):
            self.y+=1
        else:
            self.y
            
        print (self.d,self.m,self.y)

d1=date(10,11,2016)
d1+=50
