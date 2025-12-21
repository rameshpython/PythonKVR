#Number formating for signed numbers
#while displaying positive numbers,if we want to include '+' then we have to write
# {:+d} and {:+f}
# If we  use negative  -ve there is no use ,it will come same automatically

print("int value with sign:{:+d}".format(123))
print("int value with sign:{:+d}".format(-123))
print("int value with sign:{:+f}".format(123.456))
print("int value with sign:{:+f}".format(-123.456))
