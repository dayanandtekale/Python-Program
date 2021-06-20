# Parent - Child
# Super - Sub
# Base - Child

# # Single level inheritance
# class Parent:
#     def function_parent(self):
#         print("Parent Class")
    
# class Child(Parent):
#     def function_child(self):
#         print("Child Class")
    
# objChild = Child()
# objChild.function_parent()
# objChild.function_child()


# # Multi level inheritance
# class GrandParent:
#     def __init__(self, grandname):
#         self.grandname = grandname
#         # print(self)
    
# class Father(GrandParent):
#     def __init__(self, fathername, grandname):
#         self.fathername = fathername

#         GrandParent.__init__(self, grandname)

# class Child(Father):
#     def __init__(self, childname, fathername, grandname):
#         self.childname = childname

#         Father.__init__(self, fathername, grandname)

#     def print_name(self):
#         print("GrandFather Name = " + self.grandname)
#         print("Father Name = " + self.fathername)
#         print("Child Name = "+self.childname)

# father = Father('PQR', 'ABC')
# print(father.fathername, father.grandname)

# child = Child('XYZ', 'PQR', 'ABC')
# child.print_name()
# print(child.grandname)

# # Multiple inheritance
# class Father:
#     fathername = ""
#     def father_name(self, fathername):
#         print(fathername)

# class Mother:
#     mothername = ""
#     def mother_name(self, mothername):
#         print(mothername)

# class Child(Father, Mother):

#     def function(self, fathername, mothername):
#         # Father.father_name(self, fathername)
#         # Mother.mother_name(self, mothername)
#         print("Father  Name is = "+self.fathername)
#         print("Mother Name is = "+self.mothername)

# child = Child()
# # child.fathername = "XYZ"
# # child.mothername = "PQR"
# # child.function("XYZ", "PQR")
# child.father_name("XYZ")
# child.mother_name("PQR")


# Hirarchical Inheritance

# class Car():
#     def Speed(self, HP, volume):
#         print(self.name+" Speed is " + str(HP*volume))

# class BMW(Car):
#     name = "BMW"
#     def Color(self):
#         print("BMW's Color is Black")

# class Audi(Car):
#     name = "Audi"
#     def Type(self):
#         print("Audi's Sport Car")

# bmw = BMW()
# audi = Audi()
# bmw.Speed(2, 600)
# bmw.Color()
# audi.Speed(3.5,400)
# audi.Type()


# # Hybrid inheritance
# class Student():
#     def info(self, name, roll_number):
#         print(name + "'s roll number is "+str(roll_number))

# class Marks(Student):
#     def sub_total(self, sub1, sub2, sub3):
#         print("Total Marks are "+ (str(sub1 + sub2 + sub3)))

# class Sports(Student):
#     def sport_grade(self, grade):
#         print("grade is "+grade)

# class Result(Marks,Sports):
#     def final_result(self, subjects, grade):
#         sub1, sub2, sub3 = subjects
#         Marks.sub_total(self, sub1, sub2, sub3)
#         Sports.sport_grade(self, grade)


# result = Result()
# result.info("XYZ", 30)
# result.final_result((100, 68, 82), "A")