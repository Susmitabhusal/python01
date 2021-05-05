class Class1():
    # Constructors
    def __init__(self):
        self.id = 1
        self.name = "Susmita Bhusal:"
        self.address = "Minbhawan, Kathmandu"

    def __str__(self):
        return str(self.id) + "," + self.name + "," + self.address


class Class2():
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def __str__(self):
        return str(self.id) + "," + self.name + "," + self.address


class Class3():
    # initializer
    def __init__(self, id):
        self.id = id

    # setter
    def setId(self, id):
        self.id = id

    #getter
    def getId(self):
        return str(self.id)

    #__str()__
    def __str__(self):
        return str(self.id)

class Class4():

    def __init__(self,id,name,address):
        self.id = id
        self.name = name
        self.address = address


    #getter
    def getValue(self):
        return str(self.id) + "," +self.name +"," +self.address

    def getId(self):
        return str(self.id)

    #setter
    def setId(self, id):
        self.id = id

    def setValue(self,id,name,address):
        self.id = id
        self.name = name
        self.address = address


    #__str__
    def __str__(self):
        return str(self.id) + "," +self.name +"," +self.address

#default Constructors
class Class5():
    def __init__(self,id=0):
        self.id= id
    def getId(self):
        return str(self.id)
    def setId(self,id):
        self.id= id
    def __str__(self):
        return str(self.id)
#Inheritence
class Class6(Class5):
    def __init__(self,id=0,fullName="NA"):
        super().__init__(id)
        self.fullName=fullName
    def getValue(self):
        return self.fullName
    def setValue(self,fullName):
        self.fullName =fullName
    def __str__(self):
        return super(Class6, self).__str__()+"," +self.fullName