#! /usr/bin/python

lst=[0,'one',2,"three"]
lst1=lst
print(id(lst1))

lst1=list(lst)
print(id(lst1))



scores={"kohli":100,"Shewag":55,"Ghambir":85}
newScores=scores
newScores['dravid']=200
print (id(scores))
print (id(newScores))


x=10
y=x
print (id(x))
print (id(y))

x=100
print("y :",y)
print("x :",x)

print (id(x))
print (id(y))

for element in scores.keys():
    print(element, "Scored ", scores[element])



for num in range (-1,-11,-1):
    print(num)

for num in range (0,20,2):
#    if(num%2) == 0:
        print(num)



