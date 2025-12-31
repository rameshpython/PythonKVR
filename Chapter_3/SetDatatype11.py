# isdisjoint()
#Syntax: setobj1.isdisjoint(s2)
#This Function returns True Provided setobj1 and setobj2 are disjoint( There is no common elements).
#This Function returns False Provided setobj1 and setobj2 are not disjoint( There is atleast one common element).

s1={10,20,30,40}
s2={10,15,25,35}
s3={3,4,5,6}
s1.isdisjoint(s2) # False
print(s1,type(s1))

s1.isdisjoint(s3) # True
print(s1,type(s1))

s2.isdisjoint(s3) # True
print(s2,type(s2))

set().isdisjoint(set()) # True

set().isdisjoint({10,20,30}) # True

{10,20,30}.isdisjoint(set()) # True
