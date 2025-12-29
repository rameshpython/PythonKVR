# 4.remove()
#Syntax:  ListObj.remove(Value)
#This Function is used for Removing the First Occurence of the Specified Value.
#If the Specified Value does not Exist in List Object then we get ValueError

lst=[10,20,30,40,50,60,10,20,30]
print(lst,id(lst))
lst.remove(10)
print(lst,id(lst))
lst.remove(20)
print(lst,id(lst))
lst.remove(20)
print(lst,id(lst))
#lst.remove(20)---------------------ValueError: list.remove(x): x not in list
#[].remove(10)----------------------ValueError: list.remove(x): x not in list
#list().remove(10)------------------ValueError: list.remove(x): x not in list