s = "python"

a = s.index("o")
b = s.index("p")
c = s.index("thon")
d = s.index("yth")
e = s.index("yth")
#f = s.index("k") #ValueError: substring not found
#g = s.index("2")  #ValueError: substring not found
f = s.find("k")
g = s.find("2")
print(a,b,c,d,e,e,f)

s = "python is an oop language"
p = s.index("is")
q = s.index("lang")
#r = s.index("10") #ValueError: substring not found--> the character not in string we get output is Error.
r = s.find("10")  #In find(),  string search from begin to end and if the asked character not in string get (-1).

print(p,q,r)


