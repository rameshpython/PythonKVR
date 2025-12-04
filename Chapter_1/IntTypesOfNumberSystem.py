'''
>>> a = 0b0100
>>> print(a,type(a))
4 <class 'int'>
>>>
>>>
>>> a = 4
>>> b =bin(a)
>>> print(b)
0b100
>>>
>>> a = 0b100
>>> print(a,type(a))
4 <class 'int'>
>>>
>>> a = 0B10000
>>> print(a,type(a))
16 <class 'int'>
>>>
>>> a = 16
>>> b = bin(a)
>>> print(b)
0b10000
>>>
>>> a = 0b1111
>>> print(a,type(a))
15 <class 'int'>
>>>
>>>
>>> a = 15
>>> b =bin(a)
>>> print(b)
0b1111
>>>
>>>
>>> a = 14
>>> b =bin(a)
>>> print(b)
0b1110
>>>
>>> a = 19
>>> b = bin(a)
>>> print(b)
0b10011
>>>
>>> a = 50
>>> b =bin(a)
>>> print(b)
0b110010
>>>
>>>
>>>
>>> a = 0o17
>>> print(a,type(a))
15 <class 'int'>
>>>
>>> a = 15
>>> b = oct(a)
>>> print(b)
0o17
>>>
>>>
>>> a = 0o17
>>> b = bin(a)
>>> print(b)
0b1111
>>>
>>>
>>> a = 0o17
>>> b =0x(a)
  File "<python-input-55>", line 1
    b =0x(a)
        ^
SyntaxError: invalid hexadecimal literal
>>> a = 0o17
>>> b =0x(a)
  File "<python-input-57>", line 1
    b =0x(a)
        ^
SyntaxError: invalid hexadecimal literal
>>> a = 0o17
>>> b = hex(a)
>>> print(b)
0xf
>>>
>>> a = 0xf
>>> b =int(a)
>>> print(b)
15
>>>
>>>
>>> a =0o123
>>> print(a,type(a))
83 <class 'int'>
>>>
>>>
>>>
>>> a = 0b1011
>>> b = int(a)
>>> print(b)
11
>>>
>>>
>>> a = 0b0010
>>> b =int(a)
>>> print(b)
2
>>>
>>>
>>> a = 0b1110
>>> b =int(a)
>>> print(b)
14
>>>
>>>
>>> a = 0xac
>>> print(a,type(a))
172 <class 'int'>
>>>
>>>
>>> a = 0xbee
>>> print(a,type(a))
3054 <class 'int'>
>>>
>>>
>>> a = 172
>>> b = hex(a)
>>> print(b)
0xac
>>>
>>>
>>> a = ac
Traceback (most recent call last):
  File "<python-input-100>", line 1, in <module>
    a = ac
        ^^
NameError: name 'ac' is not defined. Did you mean: 'a'?
>>>
>>>
>>> a =
  File "<python-input-103>", line 1
    a =
       ^
SyntaxError: invalid syntax
>>>
>>>
>>> a =  0xAC
>>> print(a,type(a))
172 <class 'int'>
>>>
>>> a = Oxac
Traceback (most recent call last):
  File "<python-input-109>", line 1, in <module>
    a = Oxac
        ^^^^
NameError: name 'Oxac' is not defined
>>>
>>> a = 0xac
>>> print(a,type(a))
172 <class 'int'>
>>>
>>>
>>> a = 0b101100101110
>>> print(a,type(a))
2862 <class 'int'>
>>>
>>>
>>> a = 2862
>>> b = bin(a)
>>> print(b,type(b))
0b101100101110 <class 'str'>
>>>
>>>
>>> a = 2863
>>> b = bin(a)
>>> print(b,type(b))
0b101100101111 <class 'str'>
>>>
>>> a = 234
>>> b = bin(a)
>>> print(b,type(b))
0b11101010 <class 'str'>
>>>
>>>
>>> a = 243
>>> b = hex(a)
>>> print(b,type(b))
0xf3 <class 'str'>
>>>
>>> a = 0xf3
>>> b = 0c(a)
  File "<python-input-138>", line 1
    b = 0c(a)
        ^
SyntaxError: invalid decimal literal
>>> b = 0o(a)
  File "<python-input-139>", line 1
    b = 0o(a)
         ^
SyntaxError: invalid octal literal
>>>
>>>
>>> a = 0xf3
>>> b = 0o(a)
  File "<python-input-143>", line 1
    b = 0o(a)
         ^
SyntaxError: invalid octal literal
>>> a = 0xf3
>>> a = 0o(a)
  File "<python-input-145>", line 1
    a = 0o(a)
         ^
SyntaxError: invalid octal literal
>>>
>>>
>>> a = 0xf3
>>> b = bin(a)
>>> c = int(a)
>>> print(b,c,type(b,c))
Traceback (most recent call last):
  File "<python-input-151>", line 1, in <module>
    print(b,c,type(b,c))
              ~~~~^^^^^
TypeError: type() takes 1 or 3 arguments
>>> print(b,c)
0b11110011 243



'''