s = "python"
a=s[0]
b=s[-1]
c=s[len(s)-2]
d=s[-len(s)]
#e=s[len(s)] #IndexError: string index out of range
f=s[-len(s)+1]
#g=s[-len(s)-1] #IndexError: string index out of range


print(a,b,c,d,f) #g) #e)