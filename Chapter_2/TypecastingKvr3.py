# str to int type --> possible
#case:1
a = "123"
print(a,type(a))
b =  int(a)
print(b,type(b))

'''
#case:2
a = "12.45"
print(a,type(a))
b = int(a)
print(b,type(b)) #ValueError: invalid literal for int() with base 10: '123.45'



#case:3
a =  "True"
b = int(a)
print(b,type(b)) #ValueError: invalid literal for int() with base 10: 'True'

# We have to convert STRING TYPE charcters transfer to ASCII value and convert them from string to int.



#case:4
a = "2+3j"
b =  int(a)
print(b,type(b)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'




# case:5
a = "python"
print(a,type(a))
b = int(a)
print(b,type(b)) #ValueError: invalid literal for int() with base 10: 'python'

# We have to convert STRING TYPE charcters transfer to ASCII value and convert them from string to int.

'''