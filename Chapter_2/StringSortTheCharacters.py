# input : B4A1D3
# output : ABD134

s = input("Enter some string:")
s1=s2=output=''
for x in s :
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)    #sorting the string -->Means sequal way of forming A-Z OR 1-9