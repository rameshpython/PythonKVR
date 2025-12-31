# 3.discard()
#Syntax: setobject.discard(Value)
#This Function is used for Removing the Value from set Object.
#If Value  does not found in set object then we get space as a result.(we never get key Error)

s1={'NL', 34.56, 100, 10, 'RS', 'PYTHON'}
print(s1,type(s1),id(s1))

s1.discard(100)
print(s1,type(s1),id(s1))

s1.discard("RS")
print(s1,type(s1),id(s1))

s1.discard(10)
print(s1,type(s1),id(s1))

s1.discard(100)
set().discard(10)
print(s1,type(s1),id(s1))
#set().remove(10) #KeyError: 10


s1.discard("python") # In remove function in set - we get empty space when the value is not in set
print(s1,type(s1))

#s1.remove("python") #KeyError: 'python' # But in remove function in set - we get error when value not in set.
#print(s1,type(s1))
