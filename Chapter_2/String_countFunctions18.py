s = "MISSISSIPPI"

a = s.count("M")
b = s.count("I")
c = s.count("S")
d = s.count("P")
e = s.count("1")
f = s.count("3") # if in the string we have alphabets,if mention numbers find index to count ,it shows '0'output.

print(a,b,c,d,e,f)


s = 1233451234987658765
s1 =  str(s)
print(s1,type(s1))

a = s1.count("3")
b = s1.count("7")
c = s1.count("1")
#d = s1.count(5) #TypeError: count() argument 1 must be str, not int


print(a,b,c)#d)