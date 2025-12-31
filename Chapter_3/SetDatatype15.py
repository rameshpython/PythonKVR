# intersection()

#Syntax:    setObj3=setObj1.intersection(SetObj2)
#This Function takes all Common Values from Setobj1 and setobj2 and Place the resultant Elements in Setobj3.

s1={10,20,30,40}
s2={20,30,50,60}
print(s1,type(s1))
print(s2,type(s2))

s3=s1.intersection(s2)
print(s3,type(s3))

s4=s1.intersection(s2,{1,2,3,4})
print(s4,type(s4))

x = {10,20,30}.intersection({1,2,3,4}) #set() <class 'set'>
print(x,type(x))
