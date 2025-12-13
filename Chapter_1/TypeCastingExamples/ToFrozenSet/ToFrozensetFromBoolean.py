a = True
b = False
c = None
d = 0
e = 1
f = 2.3
g = d+e+f
print(g,type(g))

fs = frozenset({a,b,c,g})
print(fs,type(fs))