# get()

#Syntax: varname=dictobj.get(Key)
#This Function is used for Obtaining the Value of Value by passing the Value of Key.
#If the Value of Key does not Exist then get() returns None.

d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))

val=d1.get(10)
print(val)

val=d1.get(20)
print(val)

val=d1.get(200)
print(val)


statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG","MH":"MUM"}
print(statescaps)

cap=statescaps.get("TS")
print(cap)

cap=statescaps.get("KAR")
print(cap)

cap=statescaps.get("AMPT") # It is not in dict so we get output has None
#print(cap)------------------------------None

#print({}.get(10))---------------------None



d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1))

x = d1[10]
y = d1[40]
print(x,y)
#d1[400]