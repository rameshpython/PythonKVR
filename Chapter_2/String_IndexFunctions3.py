s = "python"

a = s.index("p") #0
b = s.index("t") #2
c = s.index("n") #5
d = s.index("h") #3

#f = s.index("2") #ValueError: substring not found
#e = s.index("k") #ValueError: substring not found
print(a,b,c,d) #e,#f)


s = "python"
x = s.index("thon")
print(x)  # 'thon' from this index() functions takes from string only first character(t)index ,and gives output.
          #output --> 2

'''
y = s.index("khon")
print(y)  #ValueError: substring not found,Because (k),CHARACTER not in the 's' .so extra character it is.Error.
'''



s = "python is an oop lang"
z = s.index('is')
p = s.index('lang')
#q = s.index('13') # ValueError: substring not found

print(z,p) #q)

