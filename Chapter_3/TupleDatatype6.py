# sorted():
#sorted():  This Function is used for Sorting the data of immutable Iterable object Like tuple,str,bytes....etc and gives
#                 the sorted data in the form of list.
#Syntax:       listobj=sorted(tuple object)

t1=(10,23,-56,-1,13,15,6,-2)
print(t1,type(t1))
#t1.sort() #AttributeError: 'tuple' object has no attribute 'sort'
x=sorted(t1)
print(x,type(x))
t1=tuple(x) # Converted  sorted list into tuple
print(t1,type(t1))

t2=t1[::-1]
print(t2,type(t2))




t1=(10,2,13,4,-5,23,56,5)
print(t1)
x=tuple(sorted(t1))
print(x,type(x))
print(t1)

y=tuple(sorted(t1)[::-1])
print(y,type(y))
#		OR
y=tuple(sorted(t1,reverse=True))
print(y,type(y))




t1=(10,-4,12,34,16,-6,0,15)
print(t1,type(t1))
l1=list(t1)
print(l1,type(l1))
l1.sort()
print(l1,type(l1))
t1=tuple(l1)
print(t1,type(t1))
t1=t1[::-1]
print(t1,type(t1))