# Comparison of strings with ( <,<=,>,>=,==,!=)

s1 = "Hello world"
s2 = "how are you"

print(s1>s2,s1<s2,s1==s2,s1>=s2,s1<=s2,s1!=s2)


s1 = input("Enter first strig:")
s2 = input("Enter second string:")
if s1 == s2:
    print("both strings are equal")
elif s1 != s2:
    print("both are not equal")
elif s1 > s2:
    print("first value great")
elif s1 >= s2:
    print("first value is greater or equal to second one")
elif s1 < s2:
    print("second value less")
elif s1 <= s2:
    print("second value is less or equal to first one")
else:
    print("None of the above")