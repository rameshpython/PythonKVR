x = 2 + 4j
y = x.real
z = x.imag

result = bytes(int(y))
result1 = bytes(bool(z))
print(result,type(result))
print(result1,type(result1))