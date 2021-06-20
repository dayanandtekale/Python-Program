#syntax:
    #filter(func, iterable)

listA = [10,20,40,50,60,100,56,48,25,79,200]
# resList = []
# for ele in listA:
#     if ele>50:
#         resList.append(ele)

# print(resList)

print(list(filter((lambda x: x>50), listA)))