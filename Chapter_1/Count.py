s = "MISSISSIPPI"
a = s.count("M")
b = s.count("I")
c = s.count("S")
d = s.count("P")
e = s.count("I",8)

print(a,b,c,d,e)


s = "abcabcabcabcadda"
a = s.count("a",7) # The index starts from 7th index number and counts after that how many 'a' values init string.
b = s.count("b",8) # The index starts from 8th index number and counts after that how many'b' values init string.
print(a)
print(b)