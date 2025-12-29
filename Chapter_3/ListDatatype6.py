# del operator
#Syntax-1:    del  MutableObject[Index]-------Index Based Removal
#Syntax-2:    del  MutableObject[Begin:End:Step]----Slice Based Removal
#Syntax-3:    del  ImmutableMutableObject ---------Deleting Element(s) + Deletes Physical Memory Space.

lst=[10,20,30,40]
print(lst,type(lst), id(lst))
del  lst[2]
print(lst,type(lst), id(lst))
del lst[-1]
print(lst,type(lst), id(lst))
del lst[0]
print(lst,type(lst), id(lst))



lst=[10,20,30,40,50,60,70,80]
print(lst,type(lst), id(lst))
del lst[3:6]
print(lst,type(lst), id(lst))
del lst[::2]
print(lst,type(lst), id(lst))

lst=[10,20,30,40,50,60,70,80]
print(lst,type(lst), id(lst))
del lst
#print(lst,type(lst), id(lst)) #NameError: name 'lst' is not defined.
#del operator w.r.t Immutable object 'str'
s="PYTHON"
#del s[0] #TypeError: 'str' object doesn't support item deletion
#del s[0:4] #TypeError: 'str' object does not support item deletion
del s