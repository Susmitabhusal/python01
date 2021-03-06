#if statements
"""
syntax
if(condition):
    statements for true

#condition
    value relational_operator value
    # ==,!=,<,>,>=,<=
    # result ->true or false


#example
num1=0 #initializer
if(num1==0): #compares equals to :value of num 1 is equals to  0
    print("Zero")
print("END")
"""

#if else
"""
syntax 
if(condition):
    Statement_for_true
else:
    Statement_for_false

#example

num1 = 2
if(num1==0):
    print("Zero")
else:
    print("others")
"""

#if ... elif statement
#syntax
"""
if(condition1):
    Statement_for_true
elif(condition2):
    Statement_for_true
elif(condition3):
    Statement_for_true
else:
    Statement_for_false
"""
#example
num1 =8
if(num1==0):
    print("zero")
elif(num1==1):
    print("one")
elif(num1==2):
    print("two")
else:
    print("others")

#nested if
"""
Syntax
if(condition1):
    if(condition2):
        Statement for true
"""
#Example
num1 =9
num2=8
num3=4
if(num1>num2):
    if(num1>num3):
        print(num1)

#if statements with logical operator
"""
if(condition1 logical_operator condition2)
    Statement_for_true

note:
-AND,OR
"""
num1 =8
num2= 5
num3 = 2
if((num1>num2) and (num1>num3)):
    print(num1)

#2. Looping Statement

count = 1
while(count<=5):
    print("Broadway Infosys")
    count+=1
 #Tasks
"""
1. print 1 to 10
2. print first no to last no
3. print sum of 1 to 10
4. print average of 1 to 10
5. print factorial of 1 to 10
6. print odd number between 1 to 10
7.print even number between 1 to 10
8. print sum of odd number between 1 to 10
9. print sum of even number between 1 to 10
"""

#for Loop
for i in range(5): # 0 to 4
    print(i)
print()
for i in range(1,6):
    print(i)

print()

for i in range(1,21,2): # 1,3,5,7,...<21
    print(i)

#nested loop
for i in range(5): # 0 t0 4
    for j in range(5): # 0 to 4
        print(i*j)
    print()
print()

#break and continue
print("---------------------")
for i in range(10):
    if i ==5:
        break
    print(i)

#continue statement
print("-----------------------")
for i in range(10):
    if i==5:
        continue
    else:
        print(i)

#pass
class Class1():
    pass

#return
def f1():
    return "hello"

#range()
print(range(10))
var1 = range(10)
print(var1)

#Unit4_Collections with for loop
list1 =[3,4,5,6,7]
for item in list1:
    print(item)
print()
tup1 =(1,5,6,9,2,3)
for item in tup1:
    print(item)
print()
set1 ={2,4,5,7,2,8,9}
for item in set1:
    print(item)

dict1 ={'id':1,'name':"Broadway info sys",'address':"Kathmandu,nepal"}
for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for item in dict1.items():
    print(item)

for key in dict1.keys():
    print(dict1[key])
for key, value in dict1.items():
    print(key,value)

from array import array

array1 = array('i',[6,7,3,4,7])
for item in array1:
    print(item)
    print()


# 1. print from 1 to 10
i = 1
while(i<=10):
    print(i)
    i+=1

# 2. print first no to last no
i=1
while(i<=10):
    print(i)
    i+=1

