# update()

#Syntax: SetObj1.update(setobj2)
#This Function is used for Adding OR Merging the Values of setobj2 with Setobj1.


s1={10,20,30,40}
s2={15,25,35}
print(s1,id(s1))

s3=s1.update(s2)
print(s3)
print(s1,id(s1))


s1={10,20,30,40}
s2={10,20,15,25}
s1.update(s2)
print(s1)


s1={10,20,30,40}
s2={10,20,30,40}
s1.update(s2)
print(s1)