#declare
str1 ="Brodway Info sys"
Str1 ='Broadway Info Sys'
Str1 = """Broadway Infosys"""
 #str1 =input("Enter any string:")
print(type(str1))
 #Reading from file (text, html, xml, ini, others)






str1="hello" #--> string acts as the array for character
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
# print(str1[5]) --> returns error if not found
print("-----Basic level exploring-----")
str1 = "susmita ,bhusal, ram,chandra,gaire"
print(str1)
print(id(str1))
print(type(str1))
print(len(str1))
print(max(str1)) # based on Ascii code
print(min(str1))

#methods
#capitalize(self, /)
"""   Return a capitalized version of the string.
    More specifically, make the first character have upper case and the rest lower case.
"""
str1 = "susmita ,Bhusal, Ram,chandra,gaire"
print("-------------Capitalize-------------------------")
var1 = str1.capitalize()
print(str1)
print(var1)

#casefold(self, /)
      # Return a version of the string suitable for caseless comparisons.
print("----------------case fold---------------------")
var2 = str1.casefold()
print(var2)

 #email = input("Enter your email :")
#password = input("enter you password :")

#login to system
#email = email.casefold()
#password = password
#print(email , password)

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

str1 ="""default is 'strict' meaning that encoding errors raise a UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and 'xmlcharrefreplace' as well as any other name registered with codecs.register_error that can handle UnicodeEncodeErrors."""
count = str1.count(" is ")
print(count)

for i in range(count):
    result = str1.index(" is ")
    print(result)
    str1 = """
    North Korea has hit out at the Biden administration as it prepares to unveil its strategy for dealing with Pyongyang and its nuclear programme.
    The foreign ministry said recent comments out of Washington showed President Joe Biden was intent on maintaining a "hostile policy".
    Earlier this week, Mr Biden called North Korea's nuclear programme a "serious threat" to global security.
    The White House says he plans to take a "calibrated" approach to North Korea.
    Spokeswoman Jen Psaki said on Friday that a review of US policy had been completed and suggested Mr Biden had learned from the experience of the previous four administrations who have tried, and failed, to get North Korea to abandon its nuclear weapons programme.
    "Our policy will not focus on achieving a grand bargain, nor will it rely on strategic patience," she said, saying that instead the US would pursue a "calibrated practical approach that is open to and will explore diplomacy" with North Korea while making "practical progress" on increasing security for the US and its allies.
    """
    count = str1.count("on")
    print(count)

#upper()--> returns all char in uppercase
print("---------------------uppercase------------------------")
str1= "Broadway Info Sys"
var4 = str1.upper()
print(var4)

#isupper()--> checks all char is in uppercase
print("-----------------Checks if upper------------------------")
print(str1.isupper())
print(var4.isupper())

print("-----------------swap case-------------")
var1 = str1.swapcase() #change char lower to upper and upper to lower
print(var1)
var2 = var1.swapcase()
print(var2)
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

print("------------------endswith | starts with-------------------")
str1 = "susmita,bhusal, ram,chandra,gaire"
var = str1.endswith('e')
print(var)
var1 = str1.endswith("bhusal",9)
print(var1)
var2 = str1.startswith("s")
print(var2)


#expandtabs()
print("------------------------expandtabs----------------")
str1 = "H\te\tl\tl\to"
var = str1.expandtabs(8)
print(var)

#note = \n New Line
      # \t Tab key

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
count = str1.count('str')
if(count>0):
    result=str1.index('str')
    print(result)
else:
    print("Not found")

#format()
print("-------------------format-----------------------")
str1 ="Broadway Infosys"
str2 ="Kathmandu, Nepal"
print(str1)
print("name :" ,str1)
print("Name :" +str1)
print("name:{}".format(str1))
print("Name :{0}".format(str1))
print("Name :{} \n Address :{}".format(str1,str2))
print(f"Name : {str1}, {str2}",)
#print("Name: %s,%s"%str1%str2)

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

#isalpha() --> first name, middle name, last name
print("---------------is apla ------------------------------")
str1 = "HelloWorld"
var = str1.isalpha()
print(var)
str1 = "Hello World !" #returns false when any special character is found
var = str1.isalpha()
print(var)
#isascii()
print("---------------is ascii-------------------------")
str1="Kathmandu" #english
result=str1.isascii()
print(result)
#isdecimal()
print("---------------------is decimal -----------------------")
txt = "\u0033" #unicode for 3 #int
x = txt.isdecimal()
print(x)

#isdigit()
print("-----------------is digit ----------------------------")
str1 ="12394"
var = str1.isdigit() #works only on int value not floating value
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
print("----------------------------is title| title ------------------------")
str1 ="Hellowelcometomyworld"
str2 ="HELLO WELCOME TO MY WORLD"
str3 = "22Hello"
str4= "This Is Python?"
print(str1.istitle())
print(str2.istitle())
print(str3.istitle())
print(str4.istitle())
var1 = str2.title()
print(var1)

#join()
    # Joins the elements of an iterable to the end of the string
print("----------------------join| partition------------------------------")
str1 = ("John", "Peter", "Vicky")
x = ",".join(str1)
print(x)

list1 =["Broad","way","Info","Sys"]
str2 = ';'.join(list1)
print(str2)

#partition -->divide in parts
str3 = str2.partition(";")
print(str3)

#ljust()
    # Returns a left justified version of the string
print("-------------------ljust-------------------------")
str1="this is the practice session of string method"
var= str1.ljust(50) #create left align after the following text
print(var, "continues the discussion")

#lstrip()
    # Returns a left trim version of the string
print("--------------------strip--------------------")
str1 ="         This is the practice session            "
var = str1.lstrip()
print("Start",var, "continue")

str1 =" broadway"
print(len(str1))
str2 = str1.lstrip()
print(len(str2))

str1 ="broadway "
print(len(str1))
str2= str1.rstrip()
print(len(str2))

str1 =" broadway "
print(len(str1))
str2 = str1.strip()
print(len(str2))

#zfill(self,width,/)
print("-------------------- zfill -----------------")
str1 = "123567" # if hamilai jati digit bhaye ne 10 ota print garnu payo bhane yo use garne
print(str1.zfill(10)) # always 0 at front




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
