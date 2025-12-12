d = 243 ,251 ,212 ,174

result = bytearray(d)
a = (result)
print(a)
print(d[2],type(result))
print(d[1],type(result))



result = bytearray(d)
num = complex(bytearray(d)[1])
num1 = complex(bytearray(d)[0])
print(num,type(num))
print(num1,type(num1))


bytearray_value = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
bytearray_value1= b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
result = complex(int.from_bytes(bytearray_value))
result1 = complex(int.from_bytes(bytearray_value1))
print(result)
print(result1)


bytearray_val_1 = b'\x00\x01'#converting from bytearray with value of encryption and typecasting into 'int'
res_1 = complex(int.from_bytes(bytearray_val_1))
print(res_1)


bytearray_val_2 = b'\x00\x10'#converting from bytearray with value of encryption and typecasting into 'int'
res_2 = complex(int.from_bytes(bytearray_val_2))
print(res_2)


bytearray_val_3 = b'\xfc\x00' b'\x01\x00\x00\x00'
res_3 = complex(int.from_bytes(bytearray_val_3))
print(res_3)



bytearray_value4 = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'b'\x01\x00\x00\x00'
result4 = complex(int.from_bytes(bytearray_value4))
print(result4)