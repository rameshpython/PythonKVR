#syntax-2 : varname=range(start,stop)
# This syntax generate range of values from START to STOP-1 by maintaining equal interval of step as 1(default step)

r = range(10,16)
print(r,type(r)) #range(10, 16) <class 'range'>
for val in r:
    print(val)


for val in range(50,58):
    print(val)


r = range(100, 106)
print(r,type(r))
a = r[0]
b = r[-1]
c = r[5]
#d = r[100] #IndexError: range object index out of range
for val in r:
    print(val)

print(a,b,c)#,d)



r[0:4]
for val in r[0:4]:
    print(val)


for val in r[0:4][::-1]:
    print(val)