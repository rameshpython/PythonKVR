# for substring in main string we are applying index() .

s = "Learning python is very  easy"

a = s.index("python") #9
b = s.index("y")      #28
c = s.index("y",4)
d = s.index("s")      #27
e = s.index("easy")   #25
# = s.index("hello")  #ValueError: substring not found
              # Error ,because in substring we find index if it is in given str we get output,otherwise get Error.

print(a,b,c,d,e) #,f)






s = "Learning python is very  easy"

a = s.rindex("o")      #13
b = s.rindex("t")      #11
c = s.rindex("y",4) #28
d = s.rindex("v")      #19
e = s.rindex("easy")   #25
# = s.index("hello")  #ValueError: substring not found
              # Error ,because in substring we find index if it is in given str we get output,otherwise get Error.

print(a,b,c,d,e) #,f)
