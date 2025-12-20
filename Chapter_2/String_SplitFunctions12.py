# split() --> This function is used for splitting the given string object data into different words and save as List.
# only space is allowed into split
#delimeters (_@#$%^,;) This function is splits and avoid this symbols from list.

s = "python is an oop lang"
s1 = s.split()
print(s1,len(s1),type(s1))


s = "12-12-2025"
dob =s.split("-")
s1 = "dob" " :"
s2 = "Day",dob[0]
s3 = "Month",dob[1]
s4 = "Year",dob[2]

print(s1,s2,s3,s4,type(dob))


s = "Apple#Banana#Kiwi/Guava"
words = s.split("#")
words1 = s.split("/")

print(words,words1)
