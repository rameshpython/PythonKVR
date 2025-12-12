c = 234 ,211 ,222,244
result = bytes(c)
num = float(bytes(c)[2])
print(result,type(result))
print(num,type(num))

'''
d = 234.4 ,226.7 ,156.8
result1 = bytes(d)     #TypeError: 'float' object cannot be interpreted as an integer
f = float(bytes(d)[1])  #TypeError: 'float' object cannot be interpreted as an integer
print(result1)
print(f,type(f))
'''

import  struct

def float_to_bytes(value):
    return bytearray(struct.pack('d', value))
float_bytes = float_to_bytes(3.74)
print(float_bytes,type(float_bytes))


def float_to_bytes(value):
    packed = struct.pack('d', value)
    return bytes(packed)
float_bytes = float_to_bytes(3.45)
print(float_bytes,type(float_bytes))