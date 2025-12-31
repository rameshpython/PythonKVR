# issuperset()
#Syntax:    setobj1.issuperset(setobj2)
#This Function returns True Provided setobj1 contains all the Elements of setobj2.
#This Function returns False  Provided setobj1 does not contains all the Elements of setobj2.

s1={10,20,30,40}
s2={20,30}
s3={30,45,15}
s1.issuperset(s2) # True
print(s1,type(s1))

s2.issuperset(s1) # False
print(s2,type(s2))

s2.issuperset(s3) # False
print(s2,type(s2))

s1.issuperset(s3) # False
print(s1,type(s1))

set().issuperset(set()) # True
{10,20,30}.issuperset(set()) # True
set().issuperset({10,20,30}) # False