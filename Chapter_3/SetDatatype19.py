# symmetric_difference()

#Syntax: setobj3=setobj1.symmetric_difference(setobj2)
#This function is used for removing the common elements from both setobj1 and setobj2 and later takes the
#--> remaining elements from  setobj1 and setobj2 and place them in setobj3.

s1={10,20,30,40}
s2={20,30,50,60}
print(s1,type(s1))
print(s2,type(s2))

s3=s1.symmetric_difference(s2)
print(s3,type(s3))

x = {10,20,30}.symmetric_difference({10,20,30})
print(x,type(x))

y = set().symmetric_difference({10,20,30})
print(y,type(y))


s1={10,20,30,40,45}
s2={10,20,30,40,50,70,90}
x = s1.symmetric_difference(s2)
print(x)


s1={10,20,30,40,45}
s2={10,20,30,40,50,70,90}
x = s1.symmetric_difference_update(s2)
print(x)