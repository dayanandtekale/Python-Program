a = [10,20,90,60,80]
max = 0
for i in a:
#     if i>max:
#         max =i
# print(max)
    if(a[i]<a[i+1]):
        max=a[i+1]
    else:
        max==a[i]
        print("The largest value is ",max)   