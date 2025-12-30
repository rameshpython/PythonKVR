s2 = {10,"Rs",34.56,True,False,2+3j,"python"}
print(s2,type(s2),id(s2))

#s2[2]=123.566 #TypeError: 'set' object does not support item Assignment
print(s2, type(s2))

#s2[3]  #TypeError: 'set' object is not subscriptable
#print(s2)


s2.add(123.45)
print(s2,type(s2),id(s2))


s2.remove(2+3j)
print(s2,type(s2),id(s2))


s1 = {}
print(s1,type(s1))


s2 = set()
print(s2,type(s2))
len(s2)



s3 = {10,23,'python',6.8}
print(s3,type(s3))
len(s3)


s="PYTHON"
s1=set(s)
print(s1,type(s1))

a=10
# s=set(a) #TypeError: 'int' object is not iterable
s=set([a])
print(s,type(s))
s=set((a,))
print(s,type(s))
len(s)