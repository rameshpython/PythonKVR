#Indexing and slicing appling on str(string) Data types.
#indexing on str(string)
s = "python"
print(s,type(s))

print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])

print(s[-1])
print(s[-3])
print(s[-5])
print(s[-6])

#print(s[10]) #IndexError: string index out of range

#print(s[-7])  #IndexError: string index out of range


s1 = "hello world"
print(s1[0])
print(s1[-1])

print(s1[len(s1)-1])

print(s1[-len(s)-1])

print(len(s1))

print(s1[-len(s1)+1])

print(-len(s1)-1)



s2 = "Hyderabad"

print((s2[0]))

print(s2[-1])

print(len(s2))

print([len(s2)])

print(s2[True])

print(s2[-True])

print([-len("Hyderabad")])