d1 = {10:"Apple",20:"Mango",30:"grapes",40:"kiwi",50:"berry"}
result = frozenset(list(d1.values())[3])
result1 = frozenset(list(d1.values())[2])
print(result,type(result))
print(result1,type(result1))



d2 = {"10":"Apple","20":"Mango","30":"grapes","40":"kiwi","50":"berry"}
result = (frozenset(list(d2.keys())[3]))
print(result,type(result))