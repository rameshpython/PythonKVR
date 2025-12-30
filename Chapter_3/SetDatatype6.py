# remove()
#Syntax:   setobject.remove(Value)
#This Function is used for Removing the Value from set Object.
#If Value  does not exist in set object then we get KeyError.
#If we call this function on empty set object then we get KeyError.

s1={'NL', 34.56, 100, 10, 'RS', 'PYTHON'}
print(s1,type(s1),id(s1))

s1.remove(100)
print(s1,type(s1),id(s1))

s1.remove(10)
print(s1,type(s1),id(s1))

s1.remove("PYTHON")
print(s1,type(s1),id(s1))

#s1.remove(234) #KeyError: 234
#print(s1,type(s1),id(s1))

#s1.remove(100) #KeyError: 100
#print(s1,type(s1),id(s1)) #If Value  does not exist in set object then we get KeyError.


#{10,20,30,40}.remove(100) #KeyError: 100
