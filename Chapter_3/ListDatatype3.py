# pre- defined functions in list

#1.append()
#Syntax:   listobject.append(value)
#This Function is used for adding the value to List Object at the end (Knowan as appending).

lst=[10,"RS",33.33]
print(lst,type(lst),id(lst))
lst.append(True)
print(lst,type(lst),id(lst))
lst.append("NL")
print(lst,type(lst),id(lst))




lst=list()
print(lst,type(lst),id(lst))
lst.append(10)
lst.append(12.34)
lst.append(True)
print(lst,type(lst),id(lst))
