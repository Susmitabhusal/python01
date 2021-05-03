from array import array
#sorting and searching in collection (array)
 #array - input from keyword
 #array - sort (ASC,DESC)
 #array - search specific number (return index)


#input from keyword
size = int(input("Enter how many data you need in this array: ?"))
list1 = []
for _ in range(size):
    list1.append(int(input()))
print(type(list1))
arr1 = array("i",list1)
print(arr1)
length = len(arr1)
#sorting the data in ascending
    #sorting in ascending order
for i in range(length):
    for j in range(i+1,length):
        if(arr1[i]>arr1[j]):
            temp = arr1[i]
            arr1[i] = arr1[j]
            arr1[j] = temp
print("array after  ass sorting",arr1)
#sorting in descending order
for i in range(length):
    for j in range(i+1,length):
        if(arr1[i]<arr1[j]):
            temp = arr1[i]
            arr1[i] = arr1[j]
            arr1[j] = temp
print("array after descending  sorting",arr1)


#searching the value in array
value =int(input("enter the value you want to search ?:"))
try:
    var1 = arr1.index(value)
    print(var1)
except:
    print("value not found search for another")



