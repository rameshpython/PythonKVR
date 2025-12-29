# inner list or nested list
lst=[[10,20,30],[40,50,60],[70,80,90]]
print(lst)
for val in lst:
    print(val)


lst=[ [[10,20,30],[40,50,60],[70,80,90]], [[1,2,3],[4,5,6],[7,8,9]] ]
print(lst)

for matrix in lst:
			print(matrix)


for matrix in lst:
    for row in matrix:
        print(row)