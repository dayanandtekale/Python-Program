a = [45, 67, 27, 92, 30, 71]
b = [91, 54, 67, 28, 71, 45]

# print(set(a).intersection(set(b)))

# for aitem in a:
#     for bitem in b:
#         if aitem==bitem:
#             print(aitem)

# print(45 in b)

for aitem in a:
    if aitem in b:
        print(aitem)
    