# def hello():
#     print("Hello")

# myfunc = hello
# myfunc()

def outer_function(func):
    x = 30
    def inner_function():
        print("This will excute first")

        func()
        print("inner function", x)

        print("This will excute Last")
    return inner_function


@outer_function
def user_function():
    x = 40
    print("This is executed from user function")
    print("user function", x)

# myfunc = outer_function(user_function)
# myfunc()
user_function()