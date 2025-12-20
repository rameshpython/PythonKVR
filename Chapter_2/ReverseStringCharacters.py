#input : hello gaganam ramesh
#output : olleh managag hsemar

s = input("Enter some string:")
l = s.split()
l1 =[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
result = ' '.join(l1)
print(result)