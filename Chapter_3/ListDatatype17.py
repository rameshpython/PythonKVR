# inner list or nested list
lst=[10,'Rossum', [30,35,25] ,  [70,65,60]  , 'JNTU'  ]
print(lst,type(lst))

for val in lst:
     print(val,"-->",type(val),"-->",type(lst))


print(lst,type(lst))

lst[2].append(38)
print(lst,type(lst))


lst[-2].insert(1,58)
print(lst,type(lst))



lst[-2][::3]


# I want merge inner list values and append to existing list
lst[2]+lst[3]
