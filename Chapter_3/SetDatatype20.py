# symmetric_difference_update()

#Syntax: setobj1.symmetric_difference_update(setobj2)
#This Function Removes the Common Elements from Both setobj1 and setobj2 and Takes the Remaining Elements
#from both Setobj1 and setobj2  and Place them setobj1 Itself.

s1={10,20,30,40}
s2={20,30,50,60}
print(s1,type(s1))
print(s2,type(s2))

s3=s1.symmetric_difference_update(s2)
print(s3,type(s3))

x = {10,20,30}.symmetric_difference_update({10,20,30})
print(x,type(x))

y = set().symmetric_difference_update({10,20,30})
print(y,type(y))





