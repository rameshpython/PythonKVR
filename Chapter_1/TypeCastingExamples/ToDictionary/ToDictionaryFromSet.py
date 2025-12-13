a = {10,20,30,40}
b = {index: value for index, value in enumerate(a)}
print(b)



b = {10,20,30,40,50}
d = {index: value for index, value in enumerate(b) }
print(d,type(d))




a = {"apple", "banana", "cherry"}
b = {value: len(value) for value in a}
print(b)



