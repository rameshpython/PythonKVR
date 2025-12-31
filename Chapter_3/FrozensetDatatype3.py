
s1={10,"RS",33.33,True}
print(s1,type(s1))

fs2=frozenset(s1)
print(fs2,type(fs2))

'''
fs2[0]
fs2[0:3] # indexing and slicing is not applicable in set and frozenet .
fs2[0]=23
'''
'''
del fs2[0]
del fs2[0:2]
'''

