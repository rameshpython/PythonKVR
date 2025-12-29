# 12.extend()
#Syntax: ListObj1.extend(ListObj2)
#This Function is used for Merging Multiple List Object(s) into single list object.
#Programatically:   listobj1.extend(listobj2,listobj3,....listobj-n)----TypeError

lst1=[10,20,30]
lst2=['RS','TR','DR']
print(lst1,id(lst1))
print(lst2,id(lst2))

lst1.extend(lst2)
print(lst1,id(lst1))

print(lst2,id(lst2))
lst2.extend(lst1)
print(lst2,id(lst2))




lst1=[10,20,30]
lst2=['RS','TR','DR']
lst3=[1.2,3.4,5.6,7.8]
#lst1.extend(lst2,lst3) #TypeError: list.extend() takes exactly one argument (2 given)
#		To solve the above Problem
lst1.extend(lst2)
lst1.extend(lst3)
print(lst1)

#OR
#Merging Multiple List Elements in single list by using + Operator

print(lst1,id(lst1))
lst1=lst1+lst2+lst3
print(lst1,id(lst1))