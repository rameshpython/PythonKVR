#-ve index [BEGIN : ]

s = "PYTHON"

a = s[-100:]
b = s[-2000:]
c = s[-True:]
d = s[False:]
e = s[1000:]
f = s[0xf:]
h = s[-0xf:]

print(a,b,c,d,e,f,h)