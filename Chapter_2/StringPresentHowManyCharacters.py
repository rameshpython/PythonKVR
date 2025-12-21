#input : ABCDEABCDEABCDEBDEE
#output : A-3,B-4,C-3,D-4,E-5

s = input("Enter the some string:")
d={}
for x in s:
    if x in d.keys():
        d[x]=d[x]+1
    else:
        d[x]=1
for k,v in d.items():
    print("{}={} Times".format(k,v))