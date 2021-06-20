#syntax:
    #map(func, iterables)

import math

# without using lambda function
listA = [1,4,9,16]
listB = [10,20,40,50]
listC = [100,200,400,500,300]
listD = ['apple', 'banana', 'chiku', 'pineapple']

# def upper(value):
#     return value.upper()

# print([x for x in (map(upper, listD))])

# print(list(map(upper, listD)))

# # with using lambda function
# print(list(map((lambda x: x*2), listA)))

# # map with multiple parameteres and iterables
print(list(map((lambda x, y, z: (x+y)*z), listA, listB, listC)))
# # 0th index - 1, 10, 100 - (1+10)*100 = 11*100 = 1100
# # 1st index - 4, 20, 200 - (4+20)*200 = 24*200 = 4800
# # 2nd index - 9, 40, 400 - (9+40)*400 = 49*400 = 19600
# # 3rd index - 16, 50, 500 - (16+50)*500 = 66*500 = 33000
# # 4th index - None, None , 300 - (None+None)*300 = (?)*300 = ?

# # zip functionality using map
# print(list(map((lambda x, y: (x, y)), listA, listB)))