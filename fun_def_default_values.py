#functions with arguments and default values
# def multi(a=10, b=20):
#     return a * b

# print(multi(5))    

# def area_of_circle(radius, pi=3.14):
#     return pi * radius * radius

# print(area_of_circle(10))


# def multi_dynamic(*args):
#     print(args)
#     mul = 1
#     for arg in args:
#         mul = mul * arg
#     return mul

# print(multi_dynamic(10, 20, 3, 4, 2, 5, 10))



# def multi_dynamic(*argv, **kwargs):
#     print(argv, kwargs)
#     # print(argv[0], argv[1])
#     for key, value in kwargs.items():
#         if key == 'key1' or key == 'key2':
#             print("First bunch of arguments")
#         if key == 'key3' or key == 'key4':
#             print("second bunch of arguments")

# multi_dynamic(10, 20, 30, key2='Two', key1='One', key3='Three', key5='Five')














# def square(a, b ,c):
#     # print(a * a)
#     return a * a

# print(square(5))


