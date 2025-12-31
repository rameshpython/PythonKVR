# isdisjoint()
# union()
# intersection()
# difference()
# symmetric_difference() # all functions  which are present in the 'set' datatype same as frozenset have it .


fs1=frozenset({10,20,30,40,50,60,70})
fs2=frozenset((100,200,300))
fs3=frozenset((10,2,3))

fs1.isdisjoint(fs2)
fs1.isdisjoint(fs3)
print(fs1,type(fs1))
print(fs2,type(fs2))

fs1.union(fs2)
print(fs1,type(fs1))

fs1.intersection(fs2)
print(fs1,type(fs1))

fs1.difference(fs2)
print(fs1,type(fs1))

fs2.difference(fs1)
print(fs2,type(fs2))

frozenset({10,20,30,40}).symmetric_difference(frozenset([10,20,50,60]) )

x = fs1|fs2
print(x,type(x))