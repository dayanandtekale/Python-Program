# class ABC():

    
#     # def calc(self, public_number, secret_number):
#     #     print(public_number+secret_number)

#     @classmethod
#     def secret_number_def(cls):
#         secret_number = 100
#         return secret_number

#     @staticmethod
#     def static_secret_number():
#         secret_number = 100
#         print("From static method "+str(secret_number))

#     def hello(self):
#         print("Hello")


# abc = ABC()
# # ABC.hello()
# ABC.static_secret_number()
# print(ABC.secret_number_def())
# # ABC.static_secret_number()
# # ABC.hello()
# # # secret_number = ABC.secret_number_def()
# # abc.calc(20, ABC.secret_number_def())



class AreaOfCircle():
    pi = 3.14
    @classmethod
    def area(cls, radius):
        return cls.pi * (radius**2)

class AreaOfCircle2(AreaOfCircle):
    pi = 3.141

print(AreaOfCircle2.area(10))