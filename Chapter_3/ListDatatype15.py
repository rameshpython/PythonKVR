# 11.sort()
#Syntax-1:   ListObj.sort()---------------------------->Used for Sorting the List Similar Type of data in Ascending order
#Syntax-2:   ListObj.sort(reverser=False)-------->Used for Sorting the List Similar Type of data in Ascending order
#Syntax-3:   ListObj.sort(reverser=True)-------->Used for Sorting the List Similar Type of data in Decending order

lst1=[10,4,15,6,11,22,12,-2]
print(lst1,id(lst1))
lst1.sort()
print(lst1,id(lst1))
lst1.reverse()
print(lst1,id(lst1))

print("--------------------------------------")

lst1=[10,4,15,6,11,22,12,-2]
print(lst1,id(lst1))
lst1.sort(reverse=True)
print(lst1,id(lst1))

print("-----------------------------------------")

lst1=[10,4,15,6,11,22,12,-2]
print(lst1,id(lst1))
lst1.sort(reverse=False)
print(lst1,id(lst1))

print("-----------------------------------------")

lst1=["Rossum","Hunter","Michel","Kinney","Trump","Dennis"]
print(lst1,id(lst1))
lst1.sort()
print(lst1,id(lst1))

print("-----------------------------------------")



lst1=["Rossum","Hunter","Michel","Kinney","Trump","Dennis"]
print(lst1,id(lst1))
lst1.sort(reverse=True)
print(lst1,id(lst1))

print("-----------------------------------------")

lst1=[10,"RS",True,2.3,2+4.5j]
print(lst1,id(lst1))
#lst1.sort() #TypeError: '<' not supported between instances of 'str' and 'int'
