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
