#from array import array
#help(array)
#help(list)
#help(str)

#count a particular string and write all the index values
str1 = """North Korea has hit out at the Biden administration."""
str2 = "a"
total_count = str1.count(str2)
print(total_count)
length = len(str1)
result =0
print("index of those values")
for i in range(total_count):
    result = str1.find(str2,result+1,length)
    print(result)


