# 7.index()
#Syntax: listobj.index(Value)
#This function gives Index of First Occurence of Specified Value of List
#If the Specified Value does not Exist then  we get ValueError.

lst=[10,20,30,40,10,30,10,20]
print(lst)
a = lst.index(10)
b = lst.index(20)
#c = lst.index(25) #ValueError: 25 is not in list
print(a,b)
#print(c)
#lst.index(200) #ValueError: 200 is not in list


a = list("MISSISSIPPI").index("I")
b = list("MISSISSIPPI").index("P")
c = list("123456")
#list("123456").index(1) #ValueError: 1 is not in list
d = list("123456").index('1')

print(a,b,c,d)