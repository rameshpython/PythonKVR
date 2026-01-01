# copy ()

#Syntax: DictObj2=DictObj1.copy()
#This Function is used for Copying the content of DictObj1 into Another Dict Obj2 (Implements Shallow Copy).

d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))

d2=d1.copy() # Shallow Copy
print(d2,type(d2),id(d2))#here we Taken another variable to save,so the id will change saving space changes in RAM.

d1[10]=12.3
d2[40]=14.4

print(d1,type(d1),id(d1))
print(d2,type(d2),id(d2))