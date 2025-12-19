#join() --> This function is used for combining or joining  list of values and other types like iterable objects.

lst = ["hyd","bang","chennai","kolkata","Delhi"]
print(lst,type(lst))
s = ""
a = s.join(lst)
s = " "
b = s.join(lst)

z = [a,b]
print(a , b,)
print(z,type(z))


t = ("Rossum","is","Father","of","python")
x =  " "
x.join(t)
p = x.join(t)

print(p)
