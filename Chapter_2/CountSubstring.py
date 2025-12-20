#Cunting substrings from given string.

s = "abcabcabcabcadda"

a = s.count("a")
b = s.count("b")
c = s.count("c")
d = s.count("d")
e = s.count("a",3)
f = s.count("a",3,7)
g = s.count("b",2,12)

print(a,b,c,d,e,f,g)