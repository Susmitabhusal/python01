from array import array

#declare and Initialize Set
set1 = set()
set1 ={1,2,4,6,7,3}

array1 = array('i',[2,3,4,6,7])
set1 = set(array1)

list1 = [2,4,6,7,8,9]
set1 = set(list1)

tup1 =(7,8,9,3,2,4,8) # It discards the repeated value
set1 = set(tup1)

print(type(set1))
print(isinstance(set1, set))
print(id(set1))
print(len(set1))
print(min(set1))
print(max(set1))
print(sum(set1))

#Methods
print("----------add----------------")
set1={5,6,7,8,9,4,2}
print(set1)
set1.add(1)
print(set1)
print()
print("-----------------update------------")
set1.update([1,2,3,4,5])
print(set1)
print()
print("--------------------discard---------")
set1.discard(6)
print(set1)
print()
print("---------------remove----------------")
set1.remove(1)
print(set1)
print()
print("----------------clear------------------")
set1.clear()
print(set1)
print()

#Set Operations
print("---------------Set Opperations-------------")
set1 ={1,2,3,4,5}
set2 = {4,5,6,7,8}

print(set1-set2)
print(set1 | set2)
print(set1 & set2)
print(set1 ^ set2)
print()
print(set1.difference(set2))
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))

print(" -'-'-'-")
list1 = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
list2 = [6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15]
set1 = set(list1)
set2 = set(list2)
print(set1)
print(set2)
print(set1 & set2) # Intersection {8, 9, 6, 7}
print(set1 | set2) # Union {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print(set1 - set2) # Difference {1, 2, 3, 4, 5}
print(set1 ^ set2) # Symmetric Difference {1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15}

