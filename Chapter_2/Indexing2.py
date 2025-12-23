s = "HYDERABAD"
a=s[0]
b=s[-1]
c=s[len("HYD")]
d=s[len("RABA")]
e=s[len("RABAD")]
f=s[True]
g=s[-True]
h=s[-len('HYDERABAD')]



print(a,b,c,d,e,f,g,h)


s = "123456"
a = s[0b0001]
b = s[4]
c = s[2]
#d = s[0xF] #IndexError: string index out of range


print(a,b,c) #d)

