a = [10,20,30,40]
b = {index: value for index, value in enumerate(a)} #enumerate is indexing the values from starting (0 to default value
print(b)                                            #Were till end what value we given.at that end point it gives index.
                                                    #so we use enumerate for that.mostly we can use in range,and itreable ones.



b = [10,20,30,40,50]
d = {index: value for index, value in enumerate(b) }
print(d,type(d))




a = ["apple", "banana", "cherry"]
b = {value: len(value) for value in a}
print(b)



a = ["a", 1, "b", 2, "c", 3]
result = {a[i]: a[i + 1] for i in range(0, len(a), 2)}
print(result)