# complex()
# complex() - is used for converting other possible type of values into complex type value .
# syntax : varname = complex(int/float/bool/str)
from idlelib.colorizer import prog_group_name_to_tag

# int to complex type --> possible
a = 10
b = complex(a)
print(b,type(b))
print(b.real)
print(b.imag)

a = 0
b =  complex(a)
print(b,type(b))