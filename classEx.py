class Test:
    # class variable
    address = 'xyz road, abc colony'

    # Constructor
    def __init__(self):
        #instance variable
        self.name = "Hello World"
        self.role = "xyz"
        self.value = 10
        print(Test.address)

    # user defined method
    def hello(self, arg1):
        abc = 'Hello'
        return arg1 +" "+ self.role
        # print(Test.address)

test = Test()
# print(test.address)
# print(test.name)
# print(test.value)
# print(test.role)
print(test.hello("Hi World"))