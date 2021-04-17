class Class1():
    pass
    # class variable
    # constructors
    # instant variable
    # functions


class Class2():
    # class variable
    id = 1
    name = "Susmita Bhusal"
    address = "Minbhawan, Kathmandu"

    # Member function
    def __str__(self):
        # return (str(id)+"," +name+ "," +address)
        return ("hello from __str__()")


class Class3():
    def f1(self):
        print("hello from f1()")

    def f2(self, num1, num2):
        num3 = num1 + num2
        print("result:", num3)

    def f3(self):
        return (30 + 40)

    def f4(self, num1, num2):
        return (num1 + num2)


class Class4():
    # initializer function - constructur
    def __init__(self):
        # instance variable
        self.id = 1
        self.name = "Broadway Info sys"
        self.address = "Kathmandu"

    def __str__(self):
        return str(self.id) + "," + self.name + "," + self.address

class Class5():
    # initializer function - constructor
    def __init__(self, id, name, address):
        # instance variable
        self.id = id
        self.name = name
        self.address = address

    def __str__(self):
        return str(self.id) + "," + self.name + "," + self.address


class Class6():
    # initializer function - constructor
    def __init__(self, id):
        # instance variable
        self.id = id

    # setter
    def setId(self, id):
        self.id = id

    # Getter
    def getId(self):
        return str(self.id)

    # str
    def __str__(self):
        return str(self.id)
