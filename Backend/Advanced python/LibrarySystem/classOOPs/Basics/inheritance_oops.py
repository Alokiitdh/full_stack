# lets create a class with its own features

class A:
    def __init__(self):
        print("Class A")
    def feature1(self):
        print("Feature 1 is Woeking")
    def feature2(self):
        print("Feature 2 is Woeking")

#child class
# The child class will inherit all the features from class A
class B(A):
    def __init__(self):
        super().__init__() # this how we can call the init of class A. This gives access to the menthods from parent class
        print("Class B")
    def feature3(self):
        print("Feature 3 is Woeking")
    def feature4(self):
        print("Feature 4 is Woeking")

#instance of the class, instances will help to access the class
# a1 = A()
a2 = B()

# a1.feature1()
# a1.feature2()

# a2 is an instance of the class B which inheruit features of class A

# a2.feature1()
# a2.feature2()
# a2.feature3()
# a2.feature4()

# print(a2.__init__())
