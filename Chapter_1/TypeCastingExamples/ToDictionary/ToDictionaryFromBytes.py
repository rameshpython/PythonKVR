a = 10
x = bytes(a)
d1 = {x : "value"}
print((d1,type(d1)))


#int is here taken as value
b = 20
y = bytes(b)
d2 = {"key" : y}
print(d2,type(d2))


x = 10
y = 20
p = bytes(x)
q = bytes(y)
d3 = {p:q}
print(d3,type(d3))