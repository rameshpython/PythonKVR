# Examples :

s1={10,20,30,10,20,60,70}
print(s1,type(s1))

fs1=frozenset(s1)
print(fs1,type(fs1))

s1={10,"RS",33.33,True}
print(s1,type(s1))

fs2=frozenset(s1)
print(fs2,type(fs2))
len(fs2)

fs3=frozenset()
print(fs3,type(fs3))
len(fs3)