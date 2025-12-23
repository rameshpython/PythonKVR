s = "123"
s1 = "abc123"
s2 = "123.45"
s3 = "ABD23.65"
s4 = "123 456" # It isdigit only but space is not allowed so we get output False.
a = s.isdigit()
b = s1.isdigit()
c = s2.isdigit()
d = s3.isdigit()
e = s4.isdigit()
print(a,b,c,d,e)


