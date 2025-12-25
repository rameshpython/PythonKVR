# syntax-3: varname=range(start,stop,step)
# This syntax generate range of values from START to STOP-1 by maintaining equal programmer specified interval
  # of  step either in forward or backward direction .

r = range(10,21,2)
print(r,type(r))

for val in r:
    print(val)

for val in range(10,55,8):
    print(val)


for val in range(10, 59, 10):
    print(val)



for val in range(10, 50, 10):
    print(val)

