
a = 235.5
b = 244.7
c = a + b
result = bytes(c) #TypeError: cannot convert 'float' object to bytes
print(result)


c = 234.5 ,211.8 ,222.6 ,244.9
result5 = bytes(c)
print(result5)
print(c[3]) #TypeError: cannot convert 'float' object to bytes


byte_val_1 = b'\x00\x01'  #converting from bytes with value of encryption and typecasting into 'int'
res_1 = float.from_bytes(byte_val_1)
print(res_1)  #TypeError: cannot convert 'float' object to bytes



c = 234,211 ,222 ,244
result = bytes(c)
print(result,type(result))
print(c[2],type(result))



c = 234 ,211 ,222 ,244
result = bytes(c)
num = float(bytes(c)[2])
num1 = float(bytes(c)[3])
print(num,type(num))
print(num1,type(num1))