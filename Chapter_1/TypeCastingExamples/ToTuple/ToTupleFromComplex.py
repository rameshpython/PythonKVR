'''
a = 2 + 3j
result = tuple(a)
print(result)  #TypeError: 'complex' object is not iterable
'''



a = 2 + 3j
b = 5 - 2j
c = 3 + 7 * 4j

t1 = (a,b,c)
print(t1,type(t1))