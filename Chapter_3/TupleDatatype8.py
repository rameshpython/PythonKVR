# list in tuple

t1=(10,"Rossum",[17,16,18],[77,78,66],"OUCET")
print(t1,type(t1))
print(t1[2],type(t1[2]))
print(t1[3],type(t1[3]))
t1[2].sort()
print(t1,type(t1))
t1[3].sort(reverse=True)
print(t1,type(t1))