from OOPS.MyClasses import *

"""
obj1 = Class1()  # object declare and initialize
print(obj1)
print(type(obj1))
print(id(obj1))
print(isinstance(obj1, Class1))
"""

obj2 = Class2()
obj3 = Class2()

print(obj2)
print(type(obj2))
print(id(obj2))
print(isinstance(obj2, Class2))
print(isinstance(obj2, Class1))

# Accessing class variable
print(obj2.id)
print(obj2.name)
print(obj2.address)
print()
print(obj3.id)
print(obj3.name)
print(obj3.address)
print()

# updating the value
obj2.id = 2
obj2.name = "Broadway infosys"
obj2.address = "kathmandu"

print(obj2.id)
print(obj2.name)
print(obj2.address)
print()

# updating the value of object 3
obj3.id = 3
obj3.name = "ABC DEF"
obj3.address = "Bhaktapur"

print(obj3.id)
print(obj3.name)
print(obj3.address)
print()

obj4 = Class3()
obj4.f1()
obj4.f2(12, 13)
var1 = obj4.f3()
print(var1)
var2 = obj4.f4(12, 12)
print(var2)
print("-----------------------------------")

# accessing the instance variable
obj5 = Class4()
print(obj5.id, obj5.name, obj5.address)

# updating the values
obj5.id = 2
obj5.name = "Susmita Bhusal"
obj5.address = "Bhaktapur"
print("-----------------------------------")
print(obj5.id, obj5.name, obj5.address)
print("-----------------------------------")
print(obj5)  # call __str()__ method
print("-----------------------------------")
obj6 = Class5(1,"Susmita","Address")
print(obj6)

obj7 =Class6(100)
print(obj7.getId())
print(obj7)
obj7.setId(102)
print(obj7.getId())
print(obj7)