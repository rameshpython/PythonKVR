lst1=[]
print(lst1,type(lst1))
len(lst1)
print(lst1,type(lst1))


lst1=[10,"RS",34.56]
print(lst1,type(lst1))
len(lst1)


s="PYTHON"
print(s,type(s))
lst1=list(s)
print(lst1,type(lst1))
len(lst1)


s="PYTHON"
lst=list([s])
print(lst,type(lst))
len(lst)



a=10
b=12.4
print(a,type(a))
print(b,type(b))
#lst=list(a) #TypeError: 'int' object is not iterable
lst=list([a])
lst1=list([b])
print(lst,type(lst))
print(lst1,type(lst1))