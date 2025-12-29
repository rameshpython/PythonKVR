# enumerate()
#Syntax:  for index,value in enumerate(Iterbale-Object):
#			print(index,"--->",value)

lst=[10,20,30,10,20,30,10,20]
print(lst)
for index,value in enumerate(lst):
		print(index,"--->",value)

print("------------------------------")

for index,value in enumerate(lst):
    if(value==10):
        print(index,"--->",value)
print("------------------------------")

for index,value in enumerate(lst):
		if(value==20):
			print(index,"--->",value)

print("------------------------------")

for ind,val in enumerate("PYTHON"):
			print(ind,"-->",val)

print("------------------------------")


for ind,val in enumerate("MISSISSIPPI"):
			print(ind,"-->",val)


for ind,val in enumerate("MISSISSIPPI"):
		if(val=="I"):
			 print(ind,"-->",val)


for ind,val in enumerate("MISSISSIPPI"):
		if(val=="S"):
			print(ind,"-->",val)