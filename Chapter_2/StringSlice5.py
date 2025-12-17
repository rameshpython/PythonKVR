s = "PYTHON"

a = s[1:-1:3]
b = s[-4:5:1]
c = s[4:-5:1] #space(' ')
e = s[-1:0:2] #space(' ')
f = s[1000:-6:2] #space(' ')
g = s[-1000:0:2] #space(' ') because BEGIN<END,FORWARD DIRECTION.

print(a,b,c,e,f,g)