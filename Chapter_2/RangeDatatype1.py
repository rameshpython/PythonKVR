# range Data type
# syntax-1 : varname=range(value)
#This syntax generate range of values from 0 to -1 by maintaining equal interval of step as 1 (default step)

r = range(6)
print(r,type(r)) #range(0, 6) <class 'range'>
for val in r:
    print(val)


for val in range(6):
    print(val)