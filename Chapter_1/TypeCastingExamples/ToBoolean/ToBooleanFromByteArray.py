a = 12
b = 13 ,14 ,15 ,16 ,234 ,233
result = bytearray(a )
result1 = bytearray(b)
print(result,type(result))
print(result1,type(result1))


c = 234 ,255 ,213 ,143
result5 = bytearray(c)
print(result5)


bytearray_value = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
bytearray_value1= b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
result = bool.from_bytes(bytearray_value)
result1 = bool.from_bytes(bytearray_value1)
print(result,type(result))
print(result1,type(result1))


bytearray_val_1 = b'\x00\x01'#converting from bytearray with value of encryption and typecasting into 'int'
res_1 = bool.from_bytes(bytearray_val_1)
print(res_1)


bytearray_val_2 = b'\x00\x10'#converting from bytearray with value of encryption and typecasting into 'int'
res_2 = bool.from_bytes(bytearray_val_2)
print(res_2)


bytearray_val_3 = b'\xfc\x00' b'\x01\x00\x00\x00'
res_3 = bool.from_bytes(bytearray_val_3)
print(res_3)



bytearray_value4 = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'b'\x01\x00\x00\x00'
result4 = bool.from_bytes(bytearray_value4)
print(result4,type(result4))


