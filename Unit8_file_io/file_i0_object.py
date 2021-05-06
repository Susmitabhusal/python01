import pickle
import sys


# write in file
def write_dict():
    try:
        example_dict = {1: "6", 2: "2", 3: "f"}
        pickle_out = open("dict.pickle", "wb")  # write in binary code
        pickle.dump(example_dict, pickle_out)
        pickle_out.close()
        print("Write dictionary on file sucessfully")
    except:
        print("Error :", sys.exc_info()[1])
    finally:
        pass


# Reading from file
def read_dict():
    try:
        pickle_in = open("dict.pickle", "rb")
        obj2 = pickle.load(pickle_in)
        print("Contents of file: ")
        print(obj2)
        print("Reading contents of file successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        pass
class Person():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __str__(self):
        return str(self.id)+"," +self.name

#Write Object on File
def write_obj():
    try:
        obj1 = Person(1,"Raj Thapa")
        file1 = open("data2.obj", 'wb') # Write Binary
        pickle.dump(obj1, file1)
        file1.close()
        print("Write object successfully")
    except:
        print("Error : "+str(sys.exc_info()[1]))
    finally:
        pass

# Append Object on File
def append_obj():
    try:
        obj2 = Person(2,"Kiran Rai")
        file1 = open("data2.obj", 'ab') # Append Binary
        pickle.dump(obj2, file1)
        file1.close()
        print("Append object successfully")
    except:
        print("Error : "+str(sys.exc_info()[1]))
    finally:
        pass


# Reading Object from File
def read_obj():
    try:
        file2 = open('data2.obj', 'rb')
        obj=pickle.load(file2)
        print(obj)
        file2.close()
        print("Read object successfully")
    except:
        print("Error : " + str(sys.exc_info()[1]))
    finally:
        pass

class Person():
    def __init__(self, id=0, name=""):
        self.id=id
        self.name=name
    def __str__(self):
        return str(self.id)+", "+self.name


# Writting Objects-1
def write_objects():
    try:
        with open('data3.obj', 'wb') as file1:
            obj1 = Person(1, "Raj Tahapa")
            obj2 = Person(2, "Rajesh Rai")
            pickle.dump(obj1, file1)
            pickle.dump(obj2, file1)
            print("Write objects on file successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        pass

def read_objects():
    try:
        with open('data3.obj', 'rb') as file1:
            while True:
                try:
                    obj = pickle.load(file1)
                    print(obj)
                except:
                    break
            print("Read objects successfully")
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        pass