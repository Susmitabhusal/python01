from array import array
#sorting and searching in collection (array)
 #array - input from keyword
 #array - sort (ASC,DESC)
 #array - search specific number (return index)

"""
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

"""
#sorting (lists)
#1. Bubble Sort
def bubble_sort(items):
    swap_again=True
    n = len(items)
    while n>0 and swap_again == True:
        n= n-1
        swap_again =False
        for i in range(n):
            if  items[i]>items[i+1]:
                items[i],items[i+1] = items[i+1],items[i]
                swap_again = True
    return items

#2.Insertion Sort
def insertion_sort(items):
    n = len(items)
    for i in range(1,n):
        value = items[i]
        j= i
        while j>0 and items[j-1]>value:
            items[j] = items[j-1]
            j = j-1
        items[j] = value
    return items

print("-----------bubble-sort------------")
items = [5,7,10,1,2,4,9,7,3,6,8]
print(items)
print(bubble_sort(items))

print("---------insertion-sort---------------")
items = [5,7,10,1,2,4,9,7,3,6,8]
print(items)
print(insertion_sort(items))

def LinearSearch(list,element):
    for i in range(len(list)):
        if list[i]==element:
            return i
    return -1

def BinarySearch(list,element):
    first =0
    last= len(list)-1
    index = -1
    while (first<=last) and (index ==-1):
        mid= (first+last)//2
        if list[mid]==element:
            index = mid
        else:
            if element<list[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

print("-------------linear search-----------------")
list=[1,23,45,32,12,34,67,87,23,83,17,3,12]
print(LinearSearch(list,12))
print("-----------------binary search---------------")
list=[1,23,45,32,12,34,67,87,23,83,17,3,12]
print(BinarySearch(list,12)) #error