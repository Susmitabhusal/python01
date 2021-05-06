import sys
# Create a file
# Open and write on file(Clear all and write)
# Open and append on file (Append at last)
# Open and read from file
#String processing - String class and methods


#data Engineering (Data Science)
#Natural Language processing (NLP)
#Machine leaening - Decision Making

# we are working on same file so no need to give path
# PATH = 'C:\\Users\\ramga\\PycharmProjects\\pythonProject\\corepython1\\Unit8_file_io'
# If we use in linux or max we use path as
 #path ="C:/Users/ramga/PycharmProjects/pythonProject/corepython1/Unit8_file_io/

FILE_NAME = 'data1.txt' #if we dont give path it create on same place we create our python file

def create_file():
    try:
        file = open(FILE_NAME, "w") # Write Mode # Create a new file
        print("File create successfully!")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        file.close()

def write_data1():
    try:
        file = open(FILE_NAME, "w")
        file.write("Hello world of File IO")
        print("Write content on file successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        file.close()

def write_data2():
    try:
        file = open(FILE_NAME, "w")
        file.writelines("Hello world of File IO Line-1")
        file.writelines("Hello world of File IO Line-2")
        print("Write content on file successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        file.close()

def write_data3():
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            file.write("First Line\n")
            file.write("Second Line\n")
            file.write("Third Line\n")
            print("Write contents on file successfully!")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        file.close()

def append_data():
    try:
        file = open(FILE_NAME, "a")
        file.write("Fourth Line\n")
        print("Append content on file successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        file.close()

def read_data1():
    try:
        file = open(FILE_NAME, "r") # read mode
        # Read first five (5) characters
        #contents = file.read(5) # read first 5 characters
        # print(contents)

        # First Line
        #contents = file.readline() # read first line only
        #print(contents)

        # All Lines
        contents = file.readlines()
        print(contents) # ['First Line\n', 'Second Line\n', 'Third Line\n', 'Fourth Line\n']
        for item in contents:
            print(item, end='')
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        file.close()

def read_data2():
    try:
        file = open(FILE_NAME, "r")
        for line in file:
            print(line, end='')
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        file.close()

