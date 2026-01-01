# items()

#Syntax: varname=DictObj.items()
#This Function is used for Obtaining (Key,Value) and place the (Key,Value) in
#LHS Varname and whose Type is <class, 'dict_items'>

d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1)

kvs=d1.items()
print(kvs,type(kvs))


for kv in kvs:
		print(kv)

print("-----------------------")

for kv in kvs:
		print(kv[0],"-->",kv[1])

print("-----------------------")

for kv in d1.items():
		print(kv[0],"-->",kv[1])

print("-----------------------")

for k,v in d1.items():
		print(k,"==>",v)