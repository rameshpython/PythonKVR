# difference_update()

#Syntax: setobj1.difference_update(setobj2)
#This Function Removes the Common Elements from Both setobj1 and setobj2 and Takes the Remaining Elements
#-->from Setobj1 and Place them setobj1 Itself.

s1={10,20,30,40}
s2={20,30,45,55}
s1.difference_update(s2)
print(s1) #{40, 10}


s1={10,20,30,40}
s2={10,20,30,40,55}
s1.difference_update(s2)
print(s1)  #set()


s1={10,20,30,40}
s2={15,25}
s1.difference_update(s2)
print(s1) #{40, 10, 20, 30}

s1.difference(s2)
print(s1)