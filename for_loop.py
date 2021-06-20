#for iterator in iterable

# a = [45, 67, 27, 92, 30, 71]
# for idx in range(len(a)):
#     print(a[idx])

# for num in a:
#     print(num)

# print(list(enumerate(a)))

# for idx, value in enumerate(a):
#     print(idx, value)


for i in range(6): #(0-5)
    for j in range(5): #(0-4) 
        print("hello")
        
        
a = [45, 67, 27, 92, 30, 71]
b = [91, 54, 67, 28, 71, 45]

# for itema in a:
#     for itemb in b:
#         if itema == itemb:
#             print(itema)

for itemb in b:
    if not itemb in a:
        print(itemb)



# for item in list1:
#     print(item)
#     for inneritem in list1[6]:
#         print(inneritem)

# for idx, item in enumerate(list1):
#     if isinstance(item, list):
#         for inneritem in item:
#             print(inneritem)
#     else:
#         print(item)

    




















# list1 = [[45, 67, 27, 92, 30, 71], 
#          [91, 54, 67, 28, 71, 45]]

# for i in range(len(list1)):
#     print(i, list1[i])


# for value in list1:
#     # print(type(value))
#     if isinstance(value, list):
#         for innervalue in value:
#             print(innervalue)
#     else:
#         print(value)

# for index, value in enumerate(list1):
#     print("List ", index)
#     for innervalue in value:
#         print(innervalue)

# for i in range(1,6):
#     print("*"*i)

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end="")
#     print()

# for i in range(1,6):
#     print("*"*i)

# for value in list1[::2]:
#     print(value)
# print(list1[::2])


# 1st stage = assignment
# 2nd stage = Check the condition
# 3rd stage = stride / hopping / increment-decrement