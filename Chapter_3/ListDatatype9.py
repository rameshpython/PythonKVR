# 6.pop()

#Syntax:   listobj.pop()
#This function is used for Removing the Last Element from List Object.
#When we call this function on empty list object then we get IndexError.

lst=[10,20,30,40,"Python",True,2+3j]
print(lst,id(lst))
lst.pop()
print(lst,id(lst))
lst.pop()
print(lst,id(lst))
lst.pop()
print(lst,id(lst))

#[].pop() #IndexError: pop from empty list
#list().pop() #IndexError: pop from empty list