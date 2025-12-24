# str to bool type

#case:1 --> possible
a = "0"
print(a,type(a))
b =  bool(a)
print(b,type(b))

#case:2 --> possible
p = ("1.2")
print(p,type(p))
q = bool(p)
print(q,type(q))
a = "0.0"
print(a,type(a))
b =  bool(a)
print(b,type(b),len(a))

#case:3 --> possible

a = "False"
print(a,type(a))
b = bool(a)
print(b,type(b))
x = "False"
print(x,type(x))
y = bool(x)
print(y,type(y))

#case:4 --> possible
a = 2+5j
print(a,type(a))
b = bool(a)
print(b,type(b))
p = 0+0j
print(p,type(p))
q = bool(p)
print(q,type(q))

#case:5 --> possible

k = "PYTHON"
print(k,type(k))
l = bool(k)
print(l,type(l))

h = " "
print(h,type(h))
o =  bool(h)
print(o,type(o))


h1 = ""
print(h1,type(h1))
o1 =  bool(h1)
print(o1,type(o1))

print(bool(float(int(12.45))))
print(bool(float(int(-12.65))))
print(bool(float(int(-12.65+12.45))))