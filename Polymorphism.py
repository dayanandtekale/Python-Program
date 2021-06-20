# Polymorphism
# - Multiple forms
# - Method Overriding
# isinstance

class Shape():
    def area(self):
        return "Area"

    def perimeter(self):
        return "Perimeter"

    def density(self):
        return "Density"

class Rectangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height

    def xyz(self):
        return "Rectangle"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4*self.side

# rect = Rectangle(3,4)
# sq = Square(4)

# sh = Shape()
print(isinstance('STR', str))

# shapes = [Rectangle(3,4), Square(4), Shape(), 'ABC']
# for sh in shapes:
#     if isinstance(sh, Shape):
#         print(sh.area())
#         print(sh.perimeter())
# print(rect.area())
# print(rect.perimeter())
# print(sq.area())
# print(sq.perimeter())
