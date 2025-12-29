# Exmples

lst1=[10,20,30,40,10,20,40,10,60,70,1.2]
print(lst1,type(lst1))
lst2=[100,"Rossum",45.67,True,2+3j]
print(lst2,type(lst2))


lst2=[100,"Rossum",45.67,True,2+3j]
print(lst2,type(lst2),id(lst2))
lst2[0]
lst2[-1]
lst2[0:4]
lst2[0]=1000 # Mutability--Index Based
print(lst2,type(lst2),id(lst2))