# pre-defined functions in dict
# clear()

#Syntax: dictobj.clear()
#This Function is used for Removing all the values from Dict Object
#When we call this Function on empty dict object then we get Space OR None as Result

d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1),len(d1))

d1.clear()
print(d1,type(d1),len(d1),id(d1))

print(d1.clear()) # None

print({}.clear()) # None

print(dict().clear()) # None