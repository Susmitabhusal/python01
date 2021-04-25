from array import array
#declare
list1 = []
print(type(list1))
list1 =list()
print(type(list1))# object initialize ->call __init__()
# iterable ->array,list,set,tuple

myArray = array('i',[1,3,5,7,8,9])
list1=list(myArray) # array to list
print(list1)

tup1 =(1,2,5,6,7,8,9) # tuple to list
list1 = list(tup1)
print(list1)

set1 ={1,2,2,5,6,3,4,6,7} # set to list
list1 = list(set1)
print(list1)

#append(self,object,/)
list1.append(12)
print(list1)
#clear

#copy
list1 =[3,4,7,9,4]
print(id(list1))
list2 =list1
print(id(list2))
list2.append(12)
print(list1)
print(list2)

#HW-explore list class and test all the methods

