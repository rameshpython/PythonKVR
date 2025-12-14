a = {10,20,30,40,True,'hello',4+5j}
x = str(a)
print(x,type(x))



# tuple of strings
s1 = {"Python", "is", "fun"}
str_from_set = str(s1)
print(str_from_set)

# tuple of numbers
s2 = {1, 2, 3}
str_from_num_set = str(s2)
print(str_from_num_set)

# Expected output:
# ['Python', 'is', 'fun']
# [1, 2, 3]


a = {10}
x = str(a)
print(x,type(x))