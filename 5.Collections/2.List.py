from array import array
#declare
list1 = []
print(type(list1))
list1=[3,4,6,7,8]
list1=([1,3,5,7,8])
list1=([1,2,3,3+5,True,"Kathmandu"])
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
print("----------------append---------------")
list1.append(12)
print(list1)

#clear
print("-------------clear--------------------")
list2 = [2,4,5,8,9]
list2.clear()
print(list2)

#copy
print("--------------copy----------------------")
list1 =[3,4,7,9,4] # referencing
print(id(list1))
list2 =list1
print(id(list2))
list2.append(12)
print(list1)
print(list2)
print("___________________")
list3 = list2.copy()
print(id(list3))
print(id(list2))

# count(self, value, /)
#Return number of occurrences of value.
print("--------------count--------------")
list1 =[2,4,7,9,0,1,2,4,7,9,2,4,7,8,9,0,3,6,8]
value = list1.count(0)
print(value)
value = list1.count(12)
print(value)


#extend(self, iterable, /)
# Extend list by appending elements from the iterable.
print("-------------extend--------------")
list1 = [1,2,4,6,8,1,2]
list2= [3,4,5,1,2,0]
list1.extend(list2)
print(list1)
tup1=(1,2,3,4,5,6,7)
list2.extend(tup1)
print(list2)
set1 ={1,2,5,6,8,9,2,12}
list1.extend(set1)
print(list1)
arr1 = ('i',[1,4,6,8,9,2,3])
list1.extend(arr1)
print(list1)

# index(self, value, start=0, stop=9223372036854775807, /)
# Return first index of value.
#      Raises ValueError if the value is not present.
print("----------- indexing ---------------------")
list1 =[1,3,3,4,2,5,6,7,4,1,3,5,6,2,4,6,4,3,2,5,4]
value = list1.index(2) #check all the list
print(value)
value = list1.index(5,0,6) #checks value 5 from 0 index to 5
print(value)
print(list1[len(list1)-1]) #first check the len then len -1 i.e. last term

import sys
data = 1
start =2
end =4
try:
    value= list1.index(data,start,end)
    print(value)
except:
    print("Error: ", sys.exc_info()[1])

# insert(self, index, object, /)
    # Insert object before index.
print("-----------------insert----------------")
list1 = [1,2,4,5,7,9,4,3,1,2,6,7,8,4,3]
list1.insert(4,12)
print(list1)
list2 =[0,1,2,3] # we can add either add a value or whole collection
list1.insert(0,list2[1]) #indexing the list 2 value to insert
print(list1)
tup1 =(1,2,3,4,5)
list2.insert(6,tup1[2]) #indexing the tuple in index 6 but it inserts at last
print(list2)
set1 ={9,8,7,6,5,4}
list2.insert(-7,set1) # if negative index is not fount store at front #indexing doesnot work here
print(list2)

# pop(self, index=-1, /)
#   Remove and return item at index (default last)
#     Raises IndexError if list is empty or index is out of range.
print("-----------------pop--------------------")
list1 = [1,2,3,4,5,6,7,8,9]
value = list1.pop() #if no indexing then pop or remove from last
print(value)
print(list1)
value1 = list1.pop(-4) #works on both positive indexing and negative indexing
print(value1)
print(list1)
import sys
try:
    value2 = list1.pop(10)
    print(value2)
    print(list1)
except:
    print("ERROR : ",sys.exc_info()[1])
list2 =[]
try:
    value2 = list2.pop(1)
    print(value2)
    print(list2)
except:
    print("ERROR : ",sys.exc_info()[1])

#remove(self, value, /)
# Remove first occurrence of value.
# Raises ValueError if the value is not present
print("-------------------remove----------------")
list1 =[1,2,3,4,6,4,2,]
list1.remove(2)
print(list1)

try:
    list1.remove()
    print(list1)
except:
    print("ERROR:-",sys.exc_info()[1])

try:
    list1.remove(12)
    print(list1)
except:
    print("ERROR:-",sys.exc_info()[1])

#reverse(self, /)
# Reverse *IN PLACE*.
print("-----------------reverse-------------------")
list1 = [1,2,3,4,5,6,7,8]
print(list1)
list1.reverse()
print(list1)

#sort(self, /, *, key=None, reverse=False)
print("----------------sort---------------------")
list1 =[5,8,5,3,2,7,9,5,1,2,4,6,8,9,0,7,6,4,3,8,9,7,5,4,3,2,9,0,8]
list1.sort()
print(list1)
list1.sort(reverse=True) #key -->
print(list1)


#Extra from w3 schools
#place holder for string
print("---------place holder for string-------")
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)


#sum of list
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum)

# Updating Value
print("------------------ update ------------------")
list1 = [3, 5, 6, 7, 2, 1]
print(list1)
list1[4]=9 #update is done by indexing the value
print(list1)

# Slicing - Return list of given range
print("------------------ Slicing ------------------")
list1 = [3, 5, 6, 7, 2, 1]
print(list1[:])
print(list1[0:])
print(list1[:9])
print(list1[::2])
print(list1[::-1])

#in or not in
print("----------------in or not in ----------------------")
list1 =["Susmita","Bhusal","Ramchandra","Gaihre"]
value = "Susmita" in list1
print(value)
value = "Swekshya" not in list1
print(value)

#concat --> USED to add the list (using + sign)
list1 =["APPLE","BALL","CAT","DOG"]
list2=["ELEPHANT","FISH","GUN","HEN"]
list3 = list2 +list1
print(list3)
list3 = list1 +list2
print(list3)

#method
#zip() #combine two list and merge it to one and combine the element
print("---------------------------Zip()-----------------------")
my_list1 = [1,2,3,4,5]
my_list2 = ['Krishna','Reeta','Rhydam','Rajan','Uttam'] # it print data upto which both have commomn len
my_list3 = list(zip(my_list1, my_list2))
print(my_list3)

print(type(my_list3))
print(len(my_list3))
print(hex(id(my_list3)))

for item in my_list3:
    print(item)

id, names = zip(*my_list3) #why we used * ?
print(id, names)