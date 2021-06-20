a = [30, 54, 67, 12, 89, 45]
b = [20, 30, 67, 21, 98]
# a = ['Apple', 'Samsung', 'Nokia', 'blackberry']
# if 'Nokia' in a:
#     print("True")

# print(a.index('Nokia'))
# if a.index('NokiA')>=0:
#     print("True")

for num1 in a:
    for num2 in b:
        if num1==num2:
            print(num1)

for num in a: 
    if num in b:
        print(num)