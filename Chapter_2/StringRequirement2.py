# input : a4k3b2
# output : aeknbd

s = input("Enter some string:")
output =''
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+chr(ord(previous)+int(x))
print(output)