lst = [10,10,20,30,40,50,10,20,30,40,50]
s1 = set(lst)
print(s1,type(s1)) # converting from list to set, all Duplicate values are removed .


lst = [10,10,20,30,40,50,10,20,30,40,50]
rgv = []
for val in lst:
    if val not in rgv:
        rgv.append(val)
print(rgv,len(rgv)) #Duplicated are not allowed to set .


s = "MISSISSIPPI"
s1 = set(s)
print(s1,type(s1)) # In 'MISSISSIPPI' Duplicates were not taken into set .


s = "MISSISSIPPI"
lst = []
for val in s:
    if val not in lst:
        lst.append(val)
print(lst)