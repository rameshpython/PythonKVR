d = {"Apple":"25","Mango":"30","Kiwi":"40","berry":"50"}
x = [bool(v) for v in d.values()]
result = bool(list(d.values())[3])
print(x)
print(result,type(result))



d = {"Apple":"25","Mango":"30","Kiwi":"40","berry":"50"}
x = bool(list(d.values())[2])
print(x,type(x))


d = {"a":"10","b":"20"}
result = bool(list(d.values())[0])
print(result,type(result))

d ={1:"hello",2:"world"}
result1 = bool(list(d.keys())[1])
print(result1,type(result1))

