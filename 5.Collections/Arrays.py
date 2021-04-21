from array import array #library import

#declare an object of array type
myArray = array('i',[3,4,6,7,8]) #declare and initialize myArray object
print(myArray)

#methos
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