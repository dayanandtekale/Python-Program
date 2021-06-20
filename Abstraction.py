# Abstraction
from abc import ABC, abstractmethod, ABCMeta, abstractclassmethod, abstractstaticmethod, abstractproperty
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

    @abstractstaticmethod
    def static_method(): pass

class Square():
    def area_square(self, side):
        return side ** 2

Shape.register(Square)
sq = Square()
print(sq.area_square(5))
print(isinstance(sq, Shape))

# class Rectangle(Shape):
#     def __init__(self, length, height):
#         self.length = length
#         self.height = height

#     def area(self):
#         return self.length * self.height
    
#     def perimeter(self):
#         return (2*self.length) + (2*self.height)

#     @staticmethod
#     def static_method():
#         return "Static Method"

# rect = Rectangle(3,4)
# print(rect.area())
# print(rect.perimeter())
# print(Rectangle.static_method())




# class CRUD(ABC):
#     @abstractmethod
#     def create(self):
#         pass

#     @abstractmethod
#     def read(self):
#         pass

#     @abstractmethod
#     def update(self):
#         pass

#     @abstractmethod
#     def delete(self):
#         pass


# class User(CRUD):
#     def create