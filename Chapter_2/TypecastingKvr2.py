# complex to int type --> Not possible

a = 2+3j
print(a,type(a))
b = int(a)
print(b,type(b))#TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
