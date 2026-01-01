# keys()

#Syntax: varname=DictObj.keys()
#This Function is used for Obtaining Values of Key and place the Values of Key in LHS Varname and whose
#Type is <class, 'dict_keys'>

statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG","MH":"MUM"}
print(statescaps)

states=statescaps.keys()
print(states,type(states))

for k in statescaps.keys():
    print(k)

print("-----------------------")

for k in states:
		print(k)

print("-----------------------")

for v in statescaps.values():
    print(v)

print("-----------------------")

for k in {10:"Apple",20:"Mango",30:"Kiwi"}.keys():
		print(k)

print("-----------------------")

for k in {10:"Apple",20:"Mango",30:"Kiwi"}.keys():
		print(k,"--->",{10:"Apple",20:"Mango",30:"Kiwi"}[k])