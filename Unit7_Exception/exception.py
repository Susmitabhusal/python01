# Errors

# 1. Syntax Error
print()
# print(  # SyntaxError: unexpected EOF while parsing
print() # Solution

# while True print('Hello world')  # SyntaxError: invalid syntax
"""
while True:
    print('Hello world')
"""

# 10 * (1/0) # ZeroDivisionError: division by zero
10 * (1/1)

# 4 + var1 *3 # NameError: name 'var1' is not defined
var1=2
print(4 + var1 *3)

# print('2' + 2) # TypeError: can only concatenate str (not "int") to str
print(int('2') + 2) # Add
print('2' + str(2)) # Concat

# 2. Runtime Error
"""
# Version-0
# input
num1 = input("Enter first no : ")
num2 = input("Enter second no : ")
# process
num3 = num1/num2 # TypeError: unsupported operand type(s) for /: 'str' and 'str'
# output
print("Result : ", num3)
"""
"""
# Version-1
# input
num1 = input("Enter first no : ")
num2 = input("Enter second no : ")
# process
num1 = float(num1)
num2 = float(num2)
num3 = num1/num2
# output
print("Result : ", num3)
"""

"""
    Enter first no : 14
    Enter second no : 7
    Result :  2.0
"""
"""
    Enter first no : 14
    Enter second no : 0
    ZeroDivisionError: float division by zero
"""

# Exception Handle
"""
# Version-2
import sys
try:
    # input
    num1 = input("Enter first no : ")
    num2 = input("Enter second no : ")
    # process
    num1 = float(num1)
    num2 = float(num2)
    num3 = num1/num2
    # output
    print("Result : ", num3)
except:
    # print(sys.exc_info()) # Return Error Message
    # (<class 'ZeroDivisionError'>, ZeroDivisionError('float division by zero'), <traceback object at 0x0000016DF4467600>)
    print("Error : ", sys.exc_info()[1])
"""

"""
# Version-3
import sys
try:
    # input
    num1 = input("Enter first no : ")
    num2 = input("Enter second no : ")
    # process
    num1 = float(num1)
    num2 = float(num2)
    num3 = num1/num2
    # output
    print("Result : ", num3)
except ValueError:
    print("Error1 : ", sys.exc_info()[1])
except ZeroDivisionError:
    print("Error2 : ", sys.exc_info()[1])
"""

"""
    Enter first no : KAhmandu
    Enter second no : 0
    Error1 :  could not convert string to float: 'KAhmandu'
"""
"""
    Enter first no : 14
    Enter second no : 0
    Error2 :  float division by zero
"""
"""
    Enter first no : 14
    Enter second no : 2
    Result :  7.0
"""

# Try, Except, and Finally Keywords
# Version-4
import sys
print("Start of program")
try:
    # input
    num1 = input("Enter first no : ")
    num2 = input("Enter second no : ")
    # process
    num1 = float(num1)
    num2 = float(num2)
    num3 = num1/num2
    # output
    print("Result : ", num3)
except ValueError:
    print("Error1 : ", sys.exc_info()[1])
except ZeroDivisionError:
    print("Error2 : ", sys.exc_info()[1])
finally:
    # variables/objects - remove
    del num1
    del num2
    del num3
    print("End of program")

# Python Program Structure
try:
    pass
    # input, process, output
except:
    pass
    # print error message
finally:
    pass
    # removes/clear resources (variable, file, network ect)


