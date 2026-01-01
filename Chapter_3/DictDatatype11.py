# values()

#Syntax:    varname=DictObj.values()
#This Function is used for Obtaining Values of Value and place the Values of Values in
#LHS Varname and whose Type is <class, 'dict_values'>

statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG","MH":"MUM"}
print(statescaps)

caps=statescaps.values()
print(caps,type(caps))

for v in caps:
		print(v)

print("-----------------------")

for v in statescaps.values():
		print(v)

print("-----------------------")

for v in {'TS': 'HYD', 'AP': 'VIJ', 'KAR': 'BANG', 'MH': 'MUM'}.values():
			print(v)