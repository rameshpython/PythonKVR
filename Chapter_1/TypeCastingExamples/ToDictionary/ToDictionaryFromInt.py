#int is taken as key
a = 10
d1 = {a : "value"}  #Here we giving dict format, for int variable 'a' .
print((d1,type(d1))) # Here 'a' int type takes as key in dict format


#int is here taken as value
b = 20
d2 = {"key" : a}
print(d2,type(d2))


x = 10
y = 20
d3 = {x:y}
print(d3,type(d3))