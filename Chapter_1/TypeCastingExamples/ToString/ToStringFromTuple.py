a = (10,20,30,40,True,'hello',4+5j)
x = str(a)
print(x,type(x))



# tuple of strings
t1 = ("Python", "is", "fun")
str_from_tuple = str(t1)
print(str_from_tuple)

# tuple of numbers
num_tuple = (1, 2, 3)
str_from_num_tuple = str(num_tuple)
print(str_from_num_tuple)

# Expected output:
# ['Python', 'is', 'fun']
# [1, 2, 3]


a = (10)
x = str(a)
print(x,type(x))