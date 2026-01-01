# popitem()

#Syntax: DictObj.popitem()
#This Function is used for Removing Last (Key,value) from Dict Object
#When we call this Function on empty dict object then we get KeyError.

d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))

d1.popitem()
print(d1,type(d1),id(d1))

d1.popitem()
print(d1,type(d1),id(d1))

d1.popitem()
print(d1,type(d1),id(d1))

d1.popitem()
print(d1,type(d1),id(d1))

#d1.popitem() # KeyError: 'popitem(): dictionary is empty'

#{}.popitem() # KeyError: 'popitem(): dictionary is empty'

#dict().popitem() # KeyError: 'popitem(): dictionary is empty'