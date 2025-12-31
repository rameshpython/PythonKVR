# pre-defined functions in frozenset are :

'''
a) copy()
b) isdisjoint()
c) issuperset()
d) issubset()
e) union()
f) intersection()
g) difference()
h) symmertic_difference()
'''

#frozenset does not contain the following functions are :
'''
a) clear()
b) add()
c) remove()
d) discard()
e) pop()
f) update()
h) symmertic_difference_update()
i) difference_update()
'''
# =>If we call the above Functions by using fronzenset object then we get AttributeError

fs1=frozenset({10,20,30,409})
print(fs1,type(fs1),id(fs1))

fs2=fs1.copy()  # Deep Copy --> same id to both fs1 and fs2
print(fs2,type(fs2),id(fs2))