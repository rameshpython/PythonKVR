# issubset()

#Syntax: setobj1.issubset(setobj2)
#This Function returns True Provided setobj2 contains all the Elements of setobj1.
#This Function returns False Provided setobj2  not containg all the Elements of setobj1.

s1={10,20,30,40}
s2={20,30}
s3={30,45,15}

s2.issubset(s1) # True
print(s2,type(s2))

s1.issubset(s2) # False
print(s1,type(s1))

s3.issubset(s2) # False
print(s3,type(s3))

s3.issubset(s1) # False
print(s3,type(s3))

set().issubset(set()) # True
set().issubset({10,20,30}) # True


