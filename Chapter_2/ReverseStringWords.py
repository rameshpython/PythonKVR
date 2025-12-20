#input : Learning python is very easy
#output : easy very is python Learning

s = input("Enter some string:")
l = s.split()
l1 = []   #Taken empty list
i=len(l)-1   # This is type of [::-1] get backward direction from -1 .
while i>=0:  # length of string BEGIN- 0 ,END -1 -->backword direction comes from -1 to 0 .
             #so  i>=0 is coming -1 to 0 backword direction way.
    l1.append(l[i]) #appended values in above empty list
    i=i-1
result = ' '.join(l1)
print(result)