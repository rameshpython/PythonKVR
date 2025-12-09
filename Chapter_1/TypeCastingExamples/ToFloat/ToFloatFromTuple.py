a = 10
b = 20
c = 30
d = 40
e = 50

tpl = (10,20,30,40,50)
result = (tuple[2],type(tpl))
num = (float,tuple[2])
print(result)
print(num)

tuple = (10,20,30,40)
result = (tuple[2],type(tuple))
i = (float,tuple[3])
print(result)
print(i)


tpl = (10,20,30)
n = (float,tuple[1],type(tpl))
print(n)