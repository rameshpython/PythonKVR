d1 = {"10":"Apple","20":"Mango","30":"kiwi","40":"berry"}
num = str(d1["10"])
num1 = str(d1["30"])
print(num,type(num))
print(num1,type(num1))




d = {"Apple":"25","Mango":"30","Kiwi":"40","berry":"50"}
x = [int(v) for v in d.values()]
result = complex(list(d.values())[2])
print(x)
print(result,type(result))


d = {"Apple":"25","Mango":"30","Kiwi":"40","berry":"50"}
x = complex(list(d.values())[2])
print(x,type(x))


d = {"a":"10","b":"20"}
result = complex(list(d.values())[0])
print(result,type(result))

d ={1:"hello",2:"world"}
result1 = complex(list(d.keys())[1])
print(result1,type(result1))



d = {"1":"hello","2":"world"}
#result3 = int(list(d.values())[0])
d1 = {k:[ord(ch) for ch in v] for k,v in d.items()}
print(d1,type(d1))



d1 = {"1":"hello","2":"world"}
value = d1["1"]
result = [ord(ch) for ch in value]
print(result,type(result))

result2 = complex(ord(value[4]))
print(result2,type(result2))


