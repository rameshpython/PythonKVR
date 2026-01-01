# update ()

#Syntax: DictObj1.update(DictObj2)
#This Function is used for Updating / Merging  DictObj2 with DictObj1.

d1={10:1.2,20:2.3}
d2={30:3.3,40:4.4}
d1.update(d2)
print(d1)


d1={10:1.2,20:2.3}
d2={20:13.3,40:4.4}
d2.update(d1)
print(d2)


d1={10:11.2,20:12.3}
d2={10:1.2,20:2.3}
d1.update(d2)
print(d1)