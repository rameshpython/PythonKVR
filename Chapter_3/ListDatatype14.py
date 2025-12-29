# reverse()
#Syntax:    ListObj.reverse()
#This Function is used for Reversing the Elememts of List ( Nothing But Front goes to back and Vice-Versa)

lst1=[10,20,12,"Python",True,2+3j]
print(lst1,id(lst1))
lst2=lst1.reverse()
print(lst2)
print(lst1,id(lst1))

lst=[1,3,6,-1,0,11]
print(lst,id(lst))
lst.reverse()
print(lst,id(lst))