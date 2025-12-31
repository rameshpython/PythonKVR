# symmetric_difference_update()

s1={10,20,30,40}
s2={10,20,50,60}
s1.symmetric_difference_update(s2)
print(s1)


s1={10,20,30,40}
s2={10,20,30,40}
s1.symmetric_difference_update(s2)
print(s1)


s1={10,20,30,40}
s2={10,20,30,40,50,70,90}
s1.symmetric_difference_update(s2)
print(s1)


print("------------------------------")


s1={10,20,30,40}
s2={10,20,50,60}
s1.symmetric_difference(s2)
print(s1)

s1={10,20,30,40}
s2={10,20,30,40}
s1.symmetric_difference(s2)
print(s2)