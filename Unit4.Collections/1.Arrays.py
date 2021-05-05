from array import array # library import
from my_libs import Myfunctions
"""
#declare an object of array type
myArray = array('i',[3,4,6,7,8]) #declare and initialize myArray object
print(myArray)

#methods
#append(self,v,/)
myArray.append(12)
print(myArray)
myArray = array('i',[5,6,8,9,1,2,4,5,2,1]) #reinitializer ->remove all previous value and insrt new one
print(myArray)

#buffer_info(self)
print(myArray.buffer_info())

#count(self,v,/)
var1 = myArray.count(1)
print(var1)
print(myArray.count(2))
#extend(self,bb,/) #list, tuple - collection
myArray.append(9)
list1 =[8,9,4,5]
tup1=(2,5,6,8,9)
set1 ={1,2,3,4,1}
tmp_array = array ('i',[2,3,5,6,7])
myArray.extend(list1)
myArray.extend(tup1)
myArray.extend(set1)
myArray.extend(tmp_array)
print(myArray)

# index(self, v, /)
print(myArray.index(7))

# fromlist(self, list, /)
list2 =[4,6,7,8]
myArray.fromlist(list2)
print(myArray)

# insert(self, i, v, /)
array2 = array('i',[2,7,9,8,5,0,4,1])
print(array2.index(2))
array2.insert(0,4) #position 0th and value is 4
print(array2)
array2.insert(15,4) # insert value to last if index is not found
print(array2)

#pop(self, i=-1, /)
array2.pop(5) #delete the value from ith position 
print(array2)

#remove(self, v, /)
array2.remove(4)
print(array2)

#reverse(self,/)
array2.reverse()
print(array2)

print(array2.tobytes())

#index
var1=array2.index(2)
print(var1)
"""
"""
#example
try:
    array2 = array('i',[2,7,9,8,5,0,4,1])
    num1 = int(input("enter a number to search:"))
    result = -1 #not found
    result = array2.index(num1)
    print(result)
except:
    print("NOT FOUND")
import sys
try:
    array2 = array('i',[2,7,9,8,5,0,4,1])
    num1 = int(input("enter a number to search:"))
    result = array2.index(num1)
    print(num1 ,"Found in ",result,"index")
except:
    print("error::",sys.exc_info()[1])
  
"""
"""
my_array = array('i',[5,6,7,8,1,2,3,5,6,7])
print(my_array)
my_array.pop() #if_not_provided->remove from last
print(my_array)
my_array.pop(3)
print(my_array)

my_array = array('i',[5,6,7,8,1,2,3,5,6,7])
print(my_array)
my_array.remove(5)
print(my_array)
"""
my_array = array('i', [5, 6, 7, 8, 1, 2, 3, 5, 6, 7])
print(my_array)
my_array.reverse()  # function
print(my_array)
print(my_array[::-1])  # slicing

print(my_array.itemsize)
print(len(my_array))

print(my_array.typecode)

# exploring
# indexng
print("------indexing-----")
print(my_array[0])  # +ve indexing
print(my_array[1])
print()
print(my_array[-1])
print(my_array[-2])
# error
# print(my_array[10]) #index error out of range
# print(my_array[-11])

# error handling(exception handling
try:
    pass
except:
    pass

import sys

try:
    print(10 / 0)
except:
    print("Error:", sys.exc_info()[1])

import sys

try:
    print(my_array[-11])
except:
    print("Error:", sys.exc_info()[1])

print("------slicing-----")
myArray = array('i', [4, 2, 6, 7, 9])
print(myArray)
print(myArray[0:2])  # o to less than 2
print(myArray[1:3])  # 1 to less than 3
print(myArray[0:5:1])  # [start:end:step]
print(myArray[0:5:2])
print(myArray[::1])
print(myArray[:5:1])
print(myArray[:5:2])
print(myArray[::-1])

print("-------Referencing-------")
myArray = array('i', [4, 2, 6, 7, 9])
print(myArray)
myArray2 = myArray
print(myArray)
print(myArray2)
print(id(myArray))
print(id(myArray2))

print("-------deep copying-------")
myArray = array('i', [4, 2, 6, 7, 9])
myArray2 = array('i', [])
for item in myArray:
    myArray2.append(item)

print(id(myArray))
print(id(myArray2))
"""
def array_copy(source_array):
 destarray = array('i', [])
 for item in source_array:
        destarray.append(item)
 return destarray
"""

myArray3 = Myfunctions.array_copy(myArray2)
print(id(myArray2))
print(id(myArray3))

print("-------value updating-------")
myArray = array('i', [4, 2, 6, 7, 9])
print(myArray)
myArray[1] = 9
print(myArray)


#insert
print("-----------insert------------")
myArray = array('i', [4, 2, 6, 7, 9])
myArray.insert(2,5)
print(myArray)
print(len(myArray))
myArray.insert(7,7)
print(myArray)
print(len(myArray))

# pop(self, i=-1,/)
#return the ith element and delete it from array
print("---------------------pop-------------")
myArray = array('i', [4, 2, 6, 7, 9])
print(myArray)
result = myArray.pop(3)
print(result)
print(myArray)

# myArray.pop(5) #index # index:Error : pop index out of range
idx =4
if (len(myArray)>idx):
    myArray.pop(idx)
else:
    print("index is not availbale")

#remove(self,v,/)
#remove the first occurance of v in the array
print("---------------------remove-------------")
myArray = array('i', [4, 2, 6, 2, 9])
print(myArray)
myArray.remove(2) # remove value 2 from array
print(myArray)
myArray.remove(2) # remove value 2 for second time
print(myArray)


myArray = array('i', [4, 3, 6, 3, 9])
value =3
result = myArray.count(value) #2
print(result)
for i in range(result): #less than result
    myArray.remove(value)
print(myArray)

#reverse(self,/)
#reverse the order of item in the array.
print("-----------Reverse-----------------")
myArray = array('i',[2,3,5,6,7,8,2,3,4,5])
print(myArray)
myArray.reverse()
print(myArray)

"""#tobytes(self, /)
#convert the arrant to an array of machine value
print("------------to bytes-------------")
myArray = array('i',[1,2,3,4,5,6])
result= myArray.tobytes()
print(result)
"""


#tolist(self, /)
print("------------------tolist--------------")
myArray = array('i',[1,2,5,7,9,0])
mylist = myArray.tolist()
print(myArray)
print(type(myArray))
print(mylist)
print(type(mylist))

#tostring(self,/)
print("-----------tostring-------------")
yArray = array('i',[1,2,5,7,9,0])
myStr = myArray.tostring()
print(myArray)
print(myStr)




