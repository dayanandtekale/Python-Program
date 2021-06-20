a =[[1,2,3,4,5],[10,20,30,40,50]]
b = [[],[]]
for i in range(len(a[0])):
    if not (i==1 or i==2):
        b[0].append(a[0][i])
        b[1].append(a[1][i])
print(b)