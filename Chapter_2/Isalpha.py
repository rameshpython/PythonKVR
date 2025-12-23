s = "python"
s1 = "python34.23"
s2 = "123pyth432"
s3 = "python program" # space is not allowed we get false output.
s4 = "Gudio van rossum" # space is not allowed we get false output.
a = s.isalpha()
b = s1.isalpha()
c = s2.isalpha()
d = s3.isalpha()
e = s4.isalpha()

print(a,b,c,d,e)