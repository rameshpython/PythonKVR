# pop()

#Syntax: DictObj.pop(Key)
#This Function is used for Removing the (Key,value) from dict object by passing the Value of Key.
#If the Value of Key Does not Exist then we KeyError.

d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))

d1.pop(20)
print(d1,type(d1),id(d1))

d1.pop(30)
print(d1,type(d1),id(d1))

d1.pop(40)
print(d1,type(d1),id(d1))

#d1.pop(30) #KeyError: 30

#{}.pop(10) #KeyError: 10

#dict().pop(20) #KeyError: 20
