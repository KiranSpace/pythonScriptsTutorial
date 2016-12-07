#! /usr/bin/python


class MGM():
    def talK(self):
        print ("MGM taking")
        
class MGF():
    def teach(self):
        print("teach values")
        
class PGM():
    def talkPGM(self):
        print("tell stories")
        
class PGF():
    def talkPGF(self):
        print("encourage")
    def talk(self):
        print("PGF Speaking")

class mom(MGM,MGF):
    """class MOM"""
    global x
    global y
    x=10;y=20
    def walk(self):
        print ("Walk Elegantly: ",id(self))

    def __init__(self):
        print ("Object of class MOM")
        
    def sum(self,a,b):
        return (a+b+x+y)
        #return(a+b+self.x+self.y)
    
mymother=mom()
#print (id(mymother))
#help(mom)
#help(mymother)

class dad(PGM,PGF):
    """class DAD"""
    def talk(self):
        print ("dad speak politely")
        
    def __del__(self):
        print ("Object of class dad destroyed")
        
#mymother.walk()

class infant(mom,dad):
    """class INFANT"""
    pass


        
baby=infant()
#print(dir(baby))

baby.walk()
baby.talk()
print(baby.sum(10,20))
print(dir(baby))


