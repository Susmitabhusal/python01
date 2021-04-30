str1="hello" #--> string acts as the array for character
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
# print(str1[5]) --> returns error if not found

str1 = "susmita ,bhusal, ram,chandra,gaire"
print(str1)

#methods
#capitalize(self, /)
"""   Return a capitalized version of the string.
    More specifically, make the first character have upper case and the rest lower case.
"""
print("-------------Capitalize-------------------------")
var1 = str1.capitalize()
print(var1)

#casefold(self, /)
      # Return a version of the string suitable for caseless comparisons.
print("----------------case fold---------------------")
var2 = str1.casefold()
print(var2)
"""
     # S.count(sub[, start[, end]]) -> int
 |      
 |      #Return the number of non-overlapping occurrences of substring sub in
 |     string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation
 """
print("-------------------COUNT--------------------------------")
var3 = var2.count("s",0,len(var2))
print(var3)

#upper()--> returns all char in uppercase
print("---------------------uppercase------------------------")
var4 = str1.upper()
print(var4)
#isupper()--> checks all char is in uppercase
print("-----------------Checks if upper------------------------")
print(str1.isupper())
print(var4.isupper())

#lower()--> returns all char in lowercase
print("-----------------lowercase----------------------------")
var5 = str1.lower()
print(var5)
#islover()--> checks all char in lowercase
print("---------------------Checks if lower------------------")
print(str1.islower())
print(var5.islower())

#center(self, width, fillchar=' ', /)
print("-------------center--------------------------")
str1 = "susmita ,bhusal, ram,chandra,gaire"
print(str1)
str2 = str1.center(55)
print(str2)
str3 = str1.center(67,'#')
print(str3)

print("--------------encode------------------------")
str1 = "su$mit@ ,bhus@l, r@m,chandr@,gåire"
var = str1.encode()
print(var)

print("------------------ends with-------------------")
str1 = "susmita,bhusal, ram,chandra,gaire"
var = str1.endswith('e')
print(var)
var1 = str1.endswith("bhusal",9)
print(var1)

#exoandtabs()
print("------------------------expandtabs----------------")
str1 = "H\te\tl\tl\to"
var = str1.expandtabs(8)
print(var)

#find() # return -1 if value not found
print("------------------find------------------------")
str1 = " Hello! welcome to the python string str methods"
var = str1.find("string")
print(var)

#index() # same as find but return exception when error occur
print("-------------------index-------------------------")
str1 = "Hello ! welcome to the python string str methods"
var1 = str1.index('str')
print(var1)

#format()
print("-------------------format-----------------------")
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
txt2 = "My name is {0}, I'm {1}".format("Susmita",25)
print(txt2)
txt2 = "My name is {}, I'm {}".format("Susmita",25)
print(txt2)

#isalnum()
print("-------------is alphanumeric--------------------")
str1 ="HelloWorld12" #it returns false if space occur in the code
var = str1.isalnum()
print(var)
str1 ="HelloWorld 12" #it returns false if space occur in the code
var = str1.isalnum()
print(var)

#isalpha()
print("---------------is apla ------------------------------")
str1 = "HelloWorld"
var = str1.isalpha()
print(var)
str1 = "Hello World !" #returns false when any special character is found
var = str1.isalpha()
print(var)

#isdecimal()
print("---------------------is decimal -----------------------")
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)

#isdigit()
print("-----------------is digit ----------------------------")
str1 ="12394"
var = str1.isdigit()
print(var)

#isidentifier()
    # Returns True if the string is an identifier
print("------------------is identifier---------------------")
str1=" my dictionary"
str2 ="DICT" #it is not case sensitive
var1 = str1.isidentifier()
var2 = str2.isidentifier()
print(var1)
print(var2)

#isnumeric()
    # Returns True if all characters in the string are numeric
print("-------------------is numeric-----------------------")
str1 ="1234557" #doesnot work for deecimal
print(str1.isnumeric())

#isprintable
    # returns true if the string is printable
print("-----------------------is printable-----------------")
txt = "Hello!\nAre you #1?"
txt2 = "Hello ! how are you #1?"
print(txt.isprintable())
print(txt2.isprintable())

#isspace()
        # Returns True if all characters in the string are whitespaces
print("---------------------is space ------------------------- ")
str1 ="     "
str2="     .   "
print(str1.isspace())
print(str2.isspace())

#istitle()
    #returns true is string id tile usually check if only first char is Capital
print("----------------------------is title ------------------------")
str1 ="Hellowelcometomyworld"
str2 ="HELLO WELCOME TO MY WORLD"
str3 = "22Hello"
str4= "This Is Python?"
print(str1.istitle())
print(str2.istitle())
print(str3.istitle())
print(str4.istitle())

#join()
    # Joins the elements of an iterable to the end of the string
print("----------------------join------------------------------")
str1 = ("John", "Peter", "Vicky")
x = ",".join(str1)
print(x)

#ljust()
    # Returns a left justified version of the string
print("-------------------ljust-------------------------")
str1="this is the practice session of string method"
var= str1.ljust(50) #create left align after the following text
print(var, "continues the discussion")

#lstrip()
    # Returns a left trim version of the string
print("--------------------lstrip--------------------")
str1 ="         This is the practice session            "
var = str1.lstrip()
print("Start",var, "continue")

#maketrans() and translate()
print("------ make translation an translate--------")
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))
print("------------")
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))
