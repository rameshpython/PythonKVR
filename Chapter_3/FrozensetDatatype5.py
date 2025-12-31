# superset()
# subset() applied to the frozenset

fs1=frozenset({10,20,30,40,50,60,70})
print(fs1,type(fs1))

fs2=frozenset((10,20,30))
print(fs2,type(fs2))

fs1.issuperset(fs2) # True
print(fs1,type(fs1))

fs2.issuperset(fs1) # False
print(fs2,type(fs2))


fs2.issubset(fs1) # True
print(fs2,type(fs2))

fs1.issubset(fs2) # False
print(fs1,type(fs1))
