#user defined Exceprions
"""
#python program Template
    try:
        pass
    except:
        pass
    finally:
        pass


"""
#Example -v0
"""
import sys
try:
    #num1 =float(input("Enter any number :"))
    #Vaalidate - data type, range (min to max)
     #num1= round(num1)
    
    print("Number is :",num1)
except:
    print("Error :",sys.exc_info()[1])
finally:
    pass 
"""
#example- V1
"""
import sys

try:
    #no of students in class is 20
    #range of Roll NO is from 1 to 20
    num1 = int(input("Enter yout Roll No : "))
    if num1>=1 and num1<=20:
        print(" Roll Number is :", num1) # 1,3,8,78,0,-8
    else:
        print("Roll No out of range")
except:
    print("Error :", sys.exc_info()[1])
finally:
    pass
"""

# Example-V2
# Step-1 : Creating Exception Classes
import sys
class MyException(Exception):
    pass
class RollNoToSamll(MyException):  # <=0
    pass
class RollNoToLarge(MyException):  # >=21
    pass
# Implementation of User Defined Exceptions
try:
    print("Program Start")
    #input, process, output
    num1 = int(input("Enter Your RollNo : "))
    if (num1 <= 0):
        raise RollNoToSamll
    elif (num1 >= 21):
        raise RollNoToLarge
    else:
        print("RollNo in Range!")
except RollNoToSamll:
    print("Error : RollNo out of range - Samll")
except RollNoToLarge:
    print("Error : RollNo out of range - Large")
except:
    print("Error ", sys.exc_info()[1])
finally:
    print("program end")

#example-2 V2
# Salary range from 5000 to 12000
print("")
import sys
class   SalaryException(Exception):
    pass

class SalaryIsLess(SalaryException):
    pass
class SalaryIsMore(SalaryException):
    pass

try:
    print("Program Starts")
    salary = int(input("Enter the salary ? :"))
    if(salary<5000):
        raise SalaryIsLess
    elif(salary>12000):
        raise SalaryIsMore
    else:
        print("Salary is at range")

except SalaryIsLess:
    print("Salary is less than 5000")
except SalaryIsMore:
    print("Salary is more than 12000")
except:
    print("Error :",sys.exc_info()[1])

finally:
    print("End of the program")


