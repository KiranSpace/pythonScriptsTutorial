#! /usr/bin/python/
class PGM():
        def talkPGM(self):
                 print("Tell stories")


class PGF():
        def talkPGF(self):
                 print("Encourage")
        def talk(self):
                 print("PGF is speaking")

class MGM():
        def talk(self):
                 print("Speak softly")

class MGF():
        def Teach(self):
                 print("Teach values")
               
class Dad(PGM,PGF):
      pass
def talk(self):
      print ("speak politely")
             
class Mom(MGM,MGF):

        def __init__(self):
                print("object of Class Mom")

        
       #"""class Mom"""
        def walk(self):
                print("walk Elegantly")
        
        def sum(self,a,b):
                return(a+b)

MyMother=Mom()
print(id(MyMother))
       #help(Mom)
MyMother.walk()
#print(id(self))

class infant(Mom,Dad):
        pass
Baby=infant()
print(dir(Baby))
Baby.walk()
Baby.talk()
print(Baby.sum(10,20))



