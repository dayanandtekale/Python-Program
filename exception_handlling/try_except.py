#try-except

try:
    dict1 = {'A':1,'B':2,'C':3,'D':4,'E':5}
    # for ele in dict1:
    #     print(dict1[ele])

    # dict1['F']    

    list1 = [1,2,3,4,5]
    for ele in range(0, 5):
        print(list1[ele])
    
    # print(3/0)

    # dict1['F']  

except ZeroDivisionError as e:
    print("Error has occurred:", e)
else:
    print("Else has run")
finally:
    print("I run always")
# except ZeroDivisionError as ze:
#     print("Error has occurred:", ze)

# print("Hello")