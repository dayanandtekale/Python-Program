from functools import reduce

#syntax:
    #reduce(func, iterable, [initial_value])

#ouput:
    # (((1*2)*4)*5)*3)

# without using lambda function
listA = [1,2,4,5,3]
# def summation(prev, current):
#     print("previous value :",prev, " current Value :",current, " Sum :", prev+current)
#     return prev+current

# print(reduce(summation, listA, 10))

# with using lambda function
print(reduce((lambda x, y: x + y), listA, 10))



