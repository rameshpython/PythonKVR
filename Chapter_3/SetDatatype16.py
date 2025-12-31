# difference()

#Syntax: setobj3=setobj1.difference(setobj2)
#This Function Removes the Common Elements from Both setobj1 and setobj2 and Takes the Remaining Elements from
#->Setobj1 and Place them setobj3.

s1={10,20,30,40}
s2={20,30,50,60}
print(s1,type)
print(s2,type)

s3=s1.difference(s2)
print(s3,type(s3))

s4=s2.difference(s1)
print(s4,type(s4))

x = {10,20,30}.difference({10,20,30}) #set()
print(x,type(x))

y = {10,20,30}.difference({1,2,3}) # {10, 20, 30}
print(y,type(y))
