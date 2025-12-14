a =frozenset( {10,20,30,40,True,'hello',4+5j})
x = str(a)
print(x,type(x))



# tuple of strings
fs1 = frozenset({"Python", "is", "fun"})
str_from_frozenset = str(fs1)
print(str_from_frozenset)

# tuple of numbers
s2 = frozenset({1, 2, 3})
str_from_num_frozenset = str(s2)
print(str_from_num_frozenset)

# Expected output:
# ['Python', 'is', 'fun']
# [1, 2, 3]


a = frozenset({10})
x = str(a)
print(x,type(x))