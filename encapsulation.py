# Encapsulation

# self.variable_name - Public variable
# self._variable_name - Protected variable
# self.__variable_name - Private variable

class Encapsulate():
    __class = '3'
    def __init__(self):
        self.name = 'ABC'
        self._marks = 78
        self.__role = 'A1'
    
    def display(self):
        return self.name + " has role "+self.__role + " with marks " + str(self._marks)

    def set__role(self, rl):
        self.__role = rl

    def get__role(self):
        return self.__role


class DerivedEncapsulate():
    def __init__(self):
        Encapsulate.__init__(self)
        # print(Encapsulate._marks)
        print(self.name)



denc = DerivedEncapsulate()

# enc = Encapsulate()
# print(enc.name)
# print(enc._marks)
# enc._marks = 80
# print(enc.display())
# enc._Encapsulate__role = 'A3'
# print(enc._Encapsulate__role)
# enc.set__role('A2')
# print(enc.display())
# print(enc.get__role())