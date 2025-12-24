#converting str Bin,str Oct,str Hex into 'int' value --> possible

#case:1 -->str Bin  to int 'int' type

a = '0b1010'
print(a,type(a))
#b = int(a) #ValueError: invalid literal for int() with base 10: '0b1010'
b = int(a,2) # we have to mention base of binary ,because converting from Bin to int type .
print(b,type(b))


#case:2 --> str Oct to 'int' type

a = '0o14'
print(a,type(a))
b = int(a,8)  # Here we mentioned same as up one ,octal base 8 was mentioned.
print(b,type(b))


#case:3 --> str Hexa to 'int' type

a = '0x1c'
print(a,type(a))
b = int(a,16)  # Here we mentioned same as up one ,octal base 8 was mentioned.
print(b,type(b))

