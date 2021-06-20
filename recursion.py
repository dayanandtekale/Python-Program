import sys
# print("Get limit", sys.getrecursionlimit())
# sys.setrecursionlimit(10)
# def hello():
#     print("hello")
#     hello()

# hello()

# 5! = 5*4*3*2*1

# factorial = 1
# for num in range(5, 1, -1):
#     factorial = factorial * num

# print("factorial of 5 is",factorial)

# def fact(num):
#     if num==1:
#         return 1
#     else:
#         return num * fact(num - 1)

# print(fact(5))

sum = 0
num = 1
def fibonacci(num):
    # print(sum)
    return num + fibonacci(sum)
print(fibonacci(num))