# pre-defined functions in set
#1.add()
# Syntax: setobj.add(Value)
# This Function is used for adding the Value to set object.

s1={10,"RS",34.56}
print(s1,type(s1),id(s1))
#s1.add(200,400)#TypeError: set.add() takes exactly one argument (2 given)
s1.add(200)
print(s1,type(s1),id(s1))

s1.add("NL")
s1.add("PYTHON")
print(s1,type(s1),id(s1))