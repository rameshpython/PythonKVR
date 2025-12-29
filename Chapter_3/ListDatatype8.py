# 5.pop(index)---index based removal
#Syntax: listobj.pop(index)
#This Function removes the value from List object based on Index and It can be either +Ve OR -VE.
#If the Value of Index is Invalid then we get IndexError.

lst=[10,20,30,40,10,20,30,40]
print(lst,id(lst))
lst.pop(-1)
print(lst,id(lst))
lst.pop(3)
print(lst,id(lst))
lst.pop(-2)
print(lst,id(lst))
#lst.pop(10) #IndexError: pop index out of range
##list().pop(-1) #IndexError: pop from empty list