a =10
b = 24
c = 234
d = a + b + c
e = type(d)


print("Type-casted Int to Int : ",e)  # <class 'int'>
print("value of int :",d)




def typecasting_ToInt():
     a = 10
     b = 24
     c = 234
     d = a + b + c
     temp_type = type(d) # Temp casted variable
     temp_value =d
     return temp_type, temp_value   #list[temp_type, temp_value]


result = typecasting_ToInt()
print(result[0])  # <clss 'int'>
print(result[1])  # 268








