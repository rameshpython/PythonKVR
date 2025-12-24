# str to complex type
#case:1 --> possible
a = "12"
b = complex(a)
print(b,type(b))
print(b.real)
print(b.imag)

#case:2 --> possible
a = "12.6"
b = complex(a)
print(b,type(b))
print(b.real)
print(b.imag)

'''
#case:3 --> Not possible
a = "True"
b =  complex(a)
print(b,type(b))  #ValueError: complex() arg is a malformed string
print(b.real)
print(b.imag)
'''
#case:4 --> possible

a = "12+2.4j"
b =  complex(a)
print(b,type(b))
print(b.real)
print(b.imag)

'''
#case:5 --> Not possible
a = "python+htmlj"
b =  complex(a)
print(b,type(b)) #ValueError: complex() arg is a malformed string
print(b.real)
print(b.imag)

'''
