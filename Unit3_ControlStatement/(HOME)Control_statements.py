# if_Statements
num1=1
if(num1==0):
    print("ZERO")
print("END")

#if-else
num1=0
if(num1==0):
    print("ZERO")
else:
    print("OTHERS")

#if__elif
num1=3
if(num1==0):
    print("ZERO")
elif(num1==1):
    print("ONE")
elif(num1==2):
    print("TWO")
else:
    print("others")

#nested if
num1=12
num2=7
num3=9
if(num1>num2):
    if(num1>num3):
        print(num1)

#if statement with logical operator
num1=12
num2=7
num3=10
if(num1>num2 and num1>num3):
    print(num1)


#2. Looping Statements
#while loop
count=1
while(count<10):
    print("Broadway INFO")
    count+=1

#Questions and solutions
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

# 3. print sum from 1 to 10
i = 1
sum=0
while(i<=10):
    sum= sum+i
    i+=1
print(sum)

#4. print average of 1 to 10
i=1
sum=0
while(i<=10):
    sum= sum+i
    i+=1
avg=sum/10
print(avg)

#5. print factorial of 1 to 10
i = 1
fact=1
while(i<=10):
    fact= fact*i
    i+=1
print(fact)

# 6. print odd number between 1 to 10
i=1
while(i<=10):
    print(i)
    i+=2

# 7.print even number between 1 to 10
i=2
while(i<=10):
    print(i)
    i+=2

# 8. print sum of odd number between 1 to 10
    i = 1
    sum = 0
    while (i <= 10):
        sum = sum + i
        i += 2
    print(sum)

# 9. print sum of even number between 1 to 10
    i = 2
    sum = 0
    while (i <= 10):
        sum = sum + i
        i += 2
    print(sum)
#.for loop
for i in range(5):
    print(i)
for i in range(1,21,2):
    print(i)
for i in range(1,6):
    print(i)
#1. print 1 to 10
for i in range(1,10):
    print(i)
# 2. print first no to last no
for i in range(1,11):
    print(i)
# 3. print sum of 1 to 10
sum = 0
for i in range(1,11):
    sum = sum +i
print(sum)
# 4. print average of 1 to 10
sum = 0
for i in range(1,11):
    sum = sum +i
    avg = sum/10
print(avg)
# 5. print factorial of 1 to 10
fact = 1
for i in range (1,11):
    fact= fact*i
print(fact)
# 6. print odd number between 1 to 10
for i in range(1,10,2):
    print(i)
# 7.print even number between 1 to 10
for i in range(2,11,2):
    print(i)
# 8. print sum of odd number between 1 to 10
sum = 0
for i in range(1,10,2):
    sum = sum +i
print(sum)
# 9. print sum of even number between 1 to 10
sum = 0
for i in range(2,11,2):
    sum = sum +i
print(sum)

#looping Statement
for i in range(5):
    for j in range(5):
        print(i*j,end=' ')
    print()
print()

for i in range (5):
    for j in range(1,i):
        print("*",end=' ')
    print()
print()

#break and continue
#break
for i in range(10):
    if i==5:
        break
    print(i)

#continue
for i in range(11):
    if i==5:
        continue
    print(i)


# Collection with for loop
#list
list1 = [3,4,5,6,7]
print(list1)
for item in list1:
    print(item,end=' ')
print()

#tuple
tup1= (1,3,6,8,9)
print(tup1)
for item in tup1:
    print(item, end= ' ')
print()

#set
set1={1,5,6,8,9}
print(set1)
for item in set1:
    print(item,end=' ')
print()

#dictionary in tuple
dict1 ={'id':1, 'name': "Susmita Bhusal",'address':"Kathmandu"}

for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for item in dict1.items():
    print(item)

for key in dict1.keys():
    print(dict1[key])

for key,value in dict1.items():
    print(key,value)

#array in a loop
from array import array


array1 = array('i', [2,5,8,9,1,2])
for items in array1:
    print(items)
