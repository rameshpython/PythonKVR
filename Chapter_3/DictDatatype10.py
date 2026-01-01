# using enumerates

statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG","MH":"MUM"}
print(statescaps)

states=statescaps.keys()
print(states,type(states))

for de in enumerate(statescaps):
		print(de)

print("-----------------------")


for de in enumerate(statescaps):
		print(de,"-->",statescaps[de[1]])

print("-----------------------")

for de in enumerate(statescaps):
		print(de,"-->",statescaps.get(de[1]))