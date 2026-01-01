d1={}
print(d1,type(d1),len(d1))


d2=dict()
print(d2,type(d2),len(d2))


d1={}
print(d1,type(d1),len(d1),id(d1))
d1[100]=1.2  # Inserted Entry
d1[200]=2.2  # Inserted Entry
d1[300]=1.2  # Inserted Entry
d1[400]=4.2  # Inserted Entry
d1[500]=5.5
d1[300]=0.2
d1[300]=0.8 # I have alreaddy mentioned the 'd1[300]' but again i taken it ,so latest one is taking the key-value.

print(d1,type(d1),len(d1),id(d1))