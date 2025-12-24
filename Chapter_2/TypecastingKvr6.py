# complex to float type --> Not possible
'''
a = 2+5j
print(a,type(a))
b = float(a)
print(b,type(b)) #TypeError: float() argument must be a string or a real number, not 'complex'

a = 1.2+3.7j
print(a,type(a))
b = float(a)
print(b,type(b)) #TypeError: float() argument must be a string or a real number, not 'complex'
'''