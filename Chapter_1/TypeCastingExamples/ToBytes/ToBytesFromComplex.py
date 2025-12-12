



x = 4 + 6j#complex data type

print(x.real)#access the real part of the data

print(x.imag)#access the imaginary part of the data


a = 4 + 6j

r = a.real
s = a.imag

result = bytes(r)
result1 = bytes(int(s))
print(result)
print(result1)


g = 34
f = 75
d = g
s = f
result =  bytes(d)
result1 = bytes(s)
print(result)
print(result1)


g = 23
f = 43

e = g.real
w = f.imag

result = complex(g)
result2 = complex(49)
result3 = bytes(e)
result4 = bytes(w)
print(result)
print(result2)
print(result3)
print(result4)