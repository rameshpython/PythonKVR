a = 4 + 6j
r = a.real
s = a.imag

result = bytes(int(r))
result1 = bytes(bool(s))
print(result)
print(result1)
