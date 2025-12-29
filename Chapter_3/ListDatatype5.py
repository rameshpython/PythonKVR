# 3.clear()
#Syntax:  listobj.clear()
#This Function removes all the Elements from List Object.

lst=[10,20,30,40,"Python",True,2+3j]
print(lst,id(lst))
len(lst)
lst.clear()
print(lst,id(lst))
len(lst)



print([].clear()) #None
[].clear() #Space as Result
print(list().clear()) #None