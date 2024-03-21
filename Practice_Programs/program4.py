class Car:
    def __init__(self):
        self.name = ""

    def getString(self):
        self.input_string = input("Enter the string name: ")

    def printString(self):
        print(self.input_string.upper())


def test():
    c1=Car()
    c1.getString()
    c1.printString()

test()