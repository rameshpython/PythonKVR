# 2.insert()
#Syntax:   listobject.insert(index,Value)
#This Function is used for Adding the Value at the Specified Index.

lst=[10,"RS",33.33]
print(lst,type(lst),id(lst))
lst.insert(1,"NL")
print(lst,type(lst),id(lst))
lst.insert(0,2+3j)
print(lst,type(lst),id(lst))




lst=[10,"RS",33.33]
print(lst,type(lst),id(lst))
lst.insert(-1,"NL")
print(lst,type(lst),id(lst))