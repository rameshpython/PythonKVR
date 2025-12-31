# pop()
#Syntax: setobject.pop()
#This Function is used removing any Arbitray Element (Random Element) from non-empty set object
#When we call this function on empty set object then we get keyError .

s1={10,20,30,40,50,60,70,15}
s1.pop()
print(s1) # 70 left

s1.pop()
print(s1) # 40 left

s1.pop()
print(s1) # 10 left

s1.pop()
print(s1) # 15 left

s1.pop()
print(s1) # 50 left--> There is no indexing and slicing in set and duplicates are also not in it.
          # That's why when we use pop() - that random element from set where escaping when applied pop().







s1={'NL', 34.56, 100, 10, 'RS', 'PYTHON'}
print(s1)
s1.pop()#'NL' left
s1.pop()#34.56 left
s1.pop()#100 left
s1.pop()#10 left
s1.pop()#'RS' left
s1.pop()#'PYTHON' left
print(s1,type(s1),id(s1))#set() <class 'set'> 2021613297152
#s1.pop()#------------------------KeyError: 'pop from an empty set'
#list().pop()#--------------------IndexError: pop from empty list