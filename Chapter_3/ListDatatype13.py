# 9.copy()
#Syntax: ListObj2=ListObj1.copy()
#This Function is used for Copying the content of One ListObj1 into aonther ListObj2 (Implements Shallow Copy).

lst1=[10,"Rossum",23.45]
print(lst1,id(lst1)) #[10, 'Rossum', 23.45] 2591966192128
lst2=lst1.copy()  # Shallow Copy
print(lst2,id(lst2)) #[10, 'Rossum', 23.45] 2591966185984
lst1.append("NL")
lst2.insert(1,"HYD")
print(lst1,id(lst1)) #[10, 'Rossum', 23.45, 'NL'] 2591966192128
print(lst2,id(lst2)) #[10, 'HYD', 'Rossum', 23.45] 2591966185984

print("--------------------------------------------------------------")

#Deep copy

lst1=[10,"Rossum",23.45]
print(lst1,id(lst1)) #[10, 'Rossum', 23.45] 2591966193344
lst2=lst1 # Deep Copy
print(lst2,id(lst2)) #[10, 'Rossum', 23.45] 2591966193344
lst1.append("NL")
print(lst1,id(lst1)) #[10, 'Rossum', 23.45, 'NL'] 2591966193344
print(lst2,id(lst2)) #[10, 'Rossum', 23.45, 'NL'] 2591966193344
lst2.insert(0,"HYD")
print(lst1,id(lst1)) #['HYD', 10, 'Rossum', 23.45, 'NL'] 2591966193344
print(lst2,id(lst2)) #['HYD', 10, 'Rossum', 23.45, 'NL'] 2591966193344