#input : hello
#output :olleh

#1st way

s = input("Enter some string:")
print(s[::-1])

#2nd way

s = input("Enter some string:")
print("".join(reversed(s)))



