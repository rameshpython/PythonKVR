# int datatypes:
a = 10
print(a,type(a))

a = 20
b = 40
c = 60
print(a+b+c,type(a+b+c))


a = 20
b = 40
c = 60
d = (a+b+c)
print(d,type(d))

a = 10
b = 30.8
c = a+b
print(c,type(c))
print(int(c))

# python has implicit and explicit type of conversions

#implicit --> Means python already gives automatically conversion .It is by calculating two  types of datatypes ,finally
#comes to one type Data type it converts , without We are doing any type casting.

#Examples:

a = 5
b = 2.5
result = a+b
print(result,type(result))

x = True
y = 5
print(x+y,type(x+y))

x = False
y = 5
print(x+y,type(x+y))



#Explicit --> Means you convert the Datatype yourself by using functions
# how?--> int(), float(), str(), list(), tuple(), bytearray(), bool().
# example:

a = "25"
b = int(a)
print(b,type(b))


x = 10.7
y = int(x)
print(y,type(y))


x = 10
y = float(x)
print(y,type(y))

'''
x = 2324
y = tuple(x)
print(y,type(y))

x = 2324
y = set(x)
print(y,type(y))



x = 23.24
y = set(x)
print(y,type(y)) # fundamental datatypes are not typecast by sequence data types because ,The fundamental Data types
                 # are store single value ,so it is not iterable so fundamental data types are not accept iterable.

'''
p = 123
q = 234
t = (p,q)
print(t)


tx = (1,2,3,4,5)
print(tx)


a = 23.4
b = 34.6
c = 56
d = True
e = "ramesh"
f = 2+5j
lst = list([a,b,c,d,e,f])
print(lst)


#binary number system
#Examples:

a = 0b0100
print(a,type(a))

b = 0B10000
print(b,type(b))

c = 0b1111
print(c,type(c))

'''
d = 0b101020
print(d,type(d)) #binary allows (1,0) Digits ,base 2

'''

#octal number system
#Examples:
a = 0o17
print(a,type(a))

b = 0O123
print(b,type(b))

c = 0O561
print(c,type(c))

'''
d =0o128
print(d,type(d))
'''

#hexa decimal
#Examples:
a = 0Xac
print(a,type(a))

b = 0xbee
print(b,type(b))

c =0XFaCe
print(c,type(c))

'''
d = 0xfacer
print(d,type(d))

e = 0XAccer
print(e,type(e))
'''