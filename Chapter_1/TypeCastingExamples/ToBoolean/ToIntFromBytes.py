
a = 12
b = 13
result = bytes(a )
result1 = bytes(b)
print(result)
print(result1)

c = 234
result5 = bytes(c)
print(result5)


byte_value = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
byte_value1= b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
result = int.from_bytes(byte_value)
result1 = int.from_bytes(byte_value1)
print(result)
print(result1)


byte_val_1 = b'\x00\x01'#converting from bytes with value of encryption and typecasting into 'int'
res_1 = int.from_bytes(byte_val_1)
print(res_1)


byte_val_2 = b'\x00\x10'#converting from bytes with value of encryption and typecasting into 'int'
res_2 = int.from_bytes(byte_val_2)
print(res_2)


byte_val_3 = b'\xfc\x00'
res_3 = int.from_bytes(byte_val_3)
print(res_3)



byte_value4 = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
result4 = int.from_bytes(byte_value4)
print(result4)


