d = {"Apple":"25.4","Mango":"30.8","Kiwi":"40.3","berry":"50.6"}
x = [float(v) for v in d.values()]
result = float(list(d.values())[3])
print(x)
print(result,type(result))



d = {"Apple":"25","Mango":"30","Kiwi":"40","berry":"50"}
x = float(list(d.values())[2])
print(x,type(x))


d = {"a":"10","b":"20"}
result = float(list(d.values())[0])
print(result,type(result))

d ={1:"hello",2:"world"}
result1 = float(list(d.keys())[1])
print(result1,type(result1))



d = {"1":"hello","2":"world"}
#result3 = float(list(d.values())[0])
d1 = {k:[ord(ch) for ch in v] for k,v in d.items()}
print(d1,type(d1))



d1 = {"1":"hello","2":"world"}
value = d1["1"]
result = [ord(ch) for ch in value]
print(result,type(result))

result2 = ord(value[4])
print(result2,type(result2))

d = {"Apple":"25","Mango":"30","Kiwi":"40","berry":"50"}
x = [float(v) for v in d.values()]
result = float(list(d.values())[3])
print(x)
print(result,type(result))



d = {"Apple":"25","Mango":"30","Kiwi":"40","berry":"50"}
x = float(list(d.values())[2])
print(x,type(x))


d = {"a":"10","b":"20"}
result = float(list(d.values())[0])
print(result,type(result))

d ={1:"hello",2:"world"}
result1 = float(list(d.keys())[1])
print(result1,type(result1))



d = {"1":"hello","2":"world"}
#result3 = int(list(d.values())[0])
d1 = {k:[ord(ch) for ch in v] for k,v in d.items()}
print(d1,type(d1))



d1 = {"1":"hello","2":"world"}
value = d1["1"]
result = [ord(ch) for ch in value]
print(result,type(result))

result2 = ord(value[4])
print(result2,type(result2))