# clear()
#Syntax:   setObject.clear()
#This Function Removes all the Elements from Set Object.
#When we call this Function on empty set then we get None as Result .


s1={10,20,30,40,50,60,70,15}
print(s1) #{70, 40, 10, 15, 50, 20, 60, 30} --> left
len(s1) #8


s1.clear()
print(s1) #set()

print(s1.clear()) #None

s1.clear() #Space as Result bcoz s1 is empty

print(set().clear()) #None