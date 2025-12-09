
s = "42"
num = float(s)
print(num)


s1 = ("2346533")
num = float(s1 )
print(num)




# Binary string
s = "1010"
num = float(s)
print(num)

# Hexadecimal string
s = "A"
num = float(int(s ,16))
print(num)


s = "abc"
try:
    num = float(s)
    print(num)
except ValueError:
    print("Invalid input: cannot convert to integer")


s = "12345"
if s.isdigit():
    num = float(s)
    print(num)
else:
    print("The string is not numeric.")


v = "hello"
print(ord('h')) #  -->
print(ord('e')) #    -->
print(ord('l')) #      --> This all characters are converted each character from string to ASCII
print(ord('l')) #   -->
print(ord('o')) # -->
#o/p --> h=104 ,e=101 ,l=108 ,l=108 ,0=111  ascii values for string "hello"


print(chr(104)) # -->
print(chr(101)) #   -->
print(chr(108)) #     --> This all numbers are converted each number from int to string character
print(chr(108)) #   -->
print(chr(111)) # -->



for ch in v:
    print(ch,"=",ord(ch))


s = "hello"
ascii_characters = [ord(ch) for ch in s]
print(ascii_characters,type(ascii_characters))

result = float(ascii_characters[1])
print(result,type(result))

result1 = chr(ascii_characters[0])
print(result1,type(result1))













