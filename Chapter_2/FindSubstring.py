# Finding sub string in Given string .we use 4 methods
# FORWARD DIRECTION --> find(),index()
# BACKWARD DIRECION -->  rfind(),rindex()



# FORWARD DIRECTION --> find(),index()
s = "Learning python is very  easy"
a = s.find("python") #9
b = s.find("y")      #10
c = s.find("s")      #17
d = s.find("easy")   #25
e = s.find("hello")  # -1 ,because in substring we find index if it is in given str we get output,otherwise get (-1).

print(a,b,c,d,e)



#BACKWARD DIRECION -->  rfind(),rindex()
s = "Learning python is very  easy"

a = s.rfind("python") #9
b = s.rfind("y")      #28
c = s.rfind("s")      #27
d = s.rfind("easy")   #25
e = s.rfind("hello")  # -1 ,because in substring we find index if it is in given str we get output,otherwise get (-1).

print(a,b,c,d,e)
