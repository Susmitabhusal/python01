from OOPS.RClass import *

obj1= Class1()
print(obj1)
print(obj1.id,obj1.name,obj1.address)

obj2 = Class2(1,"Susmita BHusal","Kathamndu")
print(obj2)

obj3 = Class3(100)
print(obj3.getId())
print(obj3)
obj3.setId(102)
print(obj3)

obj4 = Class4(1,"Susmita bhusal","kathmandu")
print(obj4.getValue())
obj4.setValue(2,"ramchandra","palpa")
print(obj4)
obj4.setId(3)
print(obj4)
print(obj4.getId())
