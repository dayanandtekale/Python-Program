# class Error(Exception):
#     def __init__(self, arg1):
#         # block of code

#     def error(self, arg1):
#         # block of code

# try:
#     raise(Error())
# except Error as err:
#     print()


# class Error(Exception):
#     def __init__(self, errorcode, message):
#         self.errorcode = errorcode
#         self.message = message

class NumberIsSmall(Exception):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
a = [10, 20, 30]
try:
    a[4]
    num = int(input("Enter a Number "))
    if num<100:
        raise NumberIsSmall(100, "Number should be greater than 100")
except NumberIsSmall as e:
    print("The error has occured : ",e.expression, e.message, type(e).__name__)
except Exception as ex:
    print("The error has occured", type(ex).__name__, ex)

