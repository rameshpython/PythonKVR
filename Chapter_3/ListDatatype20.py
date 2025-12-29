# Deep copy

#To Implement Deep Copy, we use Assigment Operator (=) Only
#Syntax:    ListObj2=ListObj1

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
                     # Deep copy will not change id address while changing the variable.