a=10
print(a,type(a))
#t=tuple(a,) #TypeError: 'int' object is not iterable
#t=tuple(a) #TypeError: 'int' object is not iterable
t=tuple( (a,) )  # Valid
print(t,type(t))
#		OR
a=1.2
print(a,type(a)) #1.2 <class 'float'>
t=tuple([a])
print(t,type(t)) #(1.2,) <class 'tuple'>
