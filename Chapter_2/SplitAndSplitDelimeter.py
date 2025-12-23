s = "python is an programming lang"
x = s.split()
print(x)


s = "08-12-2025"
x = s.split()
y = s.split("-")

print(x)
print(y)
print("DD=",y[0])
print("month=",y[1])
print("year=",y[2])


s = "Apple#Mango-Kiwi#Guava"
x = s.split("#")
#print(x)
y = x[1].split("-")
#print(y)
x[1]=y[0]
#print(x)
x.insert(-1,y[1])
#print(x)


print(x)
print(y)
print(x)
print(x)
