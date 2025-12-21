#program to print characters at odd position and even position for the given string.

#1st way
s = input("Enter some string:")
print("characters at even position:",s[0::2])
print("characters at odd position:",s[1::2])

#2nd way

s = input("Enter some string:")
i  = 0
print("characters at Even position:")
while i<len(s):
    print(s[i],end=',')
    i=i+2
print()
print("characters at odd position:")
i=1
while i<len(s):
    print(s[i],end=',')
    i=i+2