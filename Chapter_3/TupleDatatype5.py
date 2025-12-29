# del operator
#NOTE:- By Using  del Operator we can't  delete values of tuple object By using Indexing and   slicing bcoz tuple object
#             belongs to Immutable But we can delete entire tuple object .


t1=(10,-34,0,10,23,56,76,21)
print(t1,type(t1))
#del t1[0] #TypeError: 'tuple' object doesn't support item deletion
#del t1[0:4] #TypeError: 'tuple' object does not support item deletion
del t1  # Here we are removing complete object.
#print(t1,type(t1)) #NameError: name 't1' is not defined
