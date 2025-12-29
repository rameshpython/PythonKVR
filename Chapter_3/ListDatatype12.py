# 8.count()
#Syntax:    listobj.count(Value)
#This function is used for Counting Number of Occurences of Specified Value.
#if Specified Value does not exist in list object then we get 0 as result.

lst=[10,20,30,10,10,30,40,20,10]
print(lst)
a = lst.count(10)
b = lst.count(20)
c = lst.count(30)
d = lst.count(40)
e = lst.count(50)
f = list("121314567").count(1)
g = list("121314567").count('1')
print(a,b,c,d,e,f,g)


x = list(["MISSISSIPPI"]).count("I")
y = list(["MISSISSIPPI"])
z = list(["MISSISSIPPI"])[0].count("I")
l = list("MISSISSIPPI").count("I")

print(x,y,z,l)