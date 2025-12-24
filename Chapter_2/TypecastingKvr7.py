# str to float type --> possible

a = "123"
print(a,type(a))
b =  float(a)
print(b,type(b))


#case:2 --> possible
a = "12.45"
print(a,type(a))
b = float(a)
print(b,type(b))


'''
#case:3 --> Not possible  
a =  "True"
print(a,type(a))
b = float(a)
print(b,type(b)) #ValueError: could not convert string to float: 'True'





#case:4 --> Not possible
a = 2+3j
print(a,type(a))
b =  float(a)
print(b,type(b)) #TypeError: float() argument must be a string or a real number, not 'complex'




# case:5 --> Not possible
a = "python3.10"
print(a,type(a))
b = float(a)
print(b,type(b)) #ValueError: could not convert string to float: 'python3.10'
'''


