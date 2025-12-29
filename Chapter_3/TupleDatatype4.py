# pre-defined functions in tuple

#Examples
#1.index()
#2.count()

t1=(10,"RS",45.67)
print(t1,type(t1))
a = t1.index(10)
b = t1.index("RS")
print(a,b)

t1=(10,"RS",45.67)
print(t1,type(t1))
c = t1.count(10)
d = t1.count(100)
print(c,d)

t1=(10,0,10,10,20,0,10)
print(t1,type(t1))
x = t1.count(10)
y = t1.count(0)
z = t1.count(100)
print(x,y,z)


t1=(10,20,30,40,50,10)
print(t1,id(t1),type(t1))
t2=t1  # Deep Copy Possible but Not Shallow Copy
print(t2,id(t2),type(t2))
t3=t1   # Deep Copy Possible but Not Shallow Copy
print(t3,id(t3),type(t3))