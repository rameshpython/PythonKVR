# shallow copy

#To Implement Shallow Copy, we use copy().
#Syntax: ListObject2=ListObj1.copy()

lst1=[10,"Rossum",23.45]
print(lst1,id(lst1)) #[10, 'Rossum', 23.45] 2591966192128
lst2=lst1.copy()  # Shallow Copy
print(lst2,id(lst2)) #[10, 'Rossum', 23.45] 2591966185984
lst1.append("NL")
lst2.insert(1,"HYD")
print(lst1,id(lst1)) #[10, 'Rossum', 23.45, 'NL'] 2591966192128
print(lst2,id(lst2)) #[10, 'HYD', 'Rossum', 23.45] 2591966185984
                     # shallow copy id will change by using different variable.

