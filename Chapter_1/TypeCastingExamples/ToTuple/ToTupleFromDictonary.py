d1 = {10:"Apple",20:"Mango",30:"grapes",40:"kiwi",50:"berry"}
result = tuple(list(d1.values())[3])
result1 = tuple(list(d1.values())[2])
print(result,type(result))
print(result1,type(result1))



d2 = {"10":"Apple","20":"Mango","30":"grapes","40":"kiwi","50":"berry"}
result = tuple(list(d2.keys())[2])
print(result,type(result))

'''
d1 = {10:"Apple",20:"Mango",30:"grapes",40:"kiwi",50:"berry"}
result = tuple(list(d1.keys())[2])
print(result,type(result)) #TypeError: 'int' object is not iterable

'''
