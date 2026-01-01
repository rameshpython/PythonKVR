
d1={10:"Apple",20:"Mango",30:"Kiwi",40:"Sberry"}
print(d1,type(d1))

#d1[0] #KeyError: 0
a = d1[10]
b = d1[20]
c = d1[30]
d = d1[40]
print(a,b,c,d)
#d1[50] #KeyError: 50


d1={10:"Apple",20:"Mango",30:"Kiwi",40:"Sberry"}
print(d1,type(d1),id(d1))

d1[10]="Guava" # # Updating Value of Value by using Value of Key
print(d1,type(d1),id(d1))
