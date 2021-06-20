def outer_function(func):
    def inner_function():
        print("This will execute first")

        func()

        print("This will execute last")

    return inner_function

@outer_function
def user_function():
    print("This is executed from user function")

# myfunc = outer_function(user_function)
# myfunc()
user_function()