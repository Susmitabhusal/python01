from my_libs import StudentFunction

var1 = StudentFunction.f1()
var2 = StudentFunction.f2()
var3 = StudentFunction.f3()
var4 = StudentFunction.f4()
var5 = StudentFunction.f5()
var6 = StudentFunction.f6()
var7 = StudentFunction.f7()
var8 = StudentFunction.f8()
var9 = StudentFunction.f9()
print("Roll no  : ", var1)
print("Name     : ", var2)
print("Class     : ", var3)
print("Section     : ", var4)
print("Marks in ")
print("sub 1     : ", var5)
print("sub 2     : ", var6)
print("sub 3     : ", var7)
print("sub4     : ", var8)
print("sub 5     : ", var9)

var10 = StudentFunction.f10(var5, var6, var7, var8, var9)
print("Total is  :",var10)

var11 = StudentFunction.f11(var10)
print("Average is  :", var11)

StudentFunction.f12(var11)
