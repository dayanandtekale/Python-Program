# def cube(n):
#     result = []
#     for i in n:
#         result.append(i**3)
#     return result

# print(cube([1,2,3,4,5]))

# def dummy():
#     for i in range(1,10):
#         print(i)
#         if i==5:
#             break
# dummy()
# dummy()
# dummy()
# dummy()
# dummy()

# def cube_generator(n):
#     for i in n:
#         yield (i**3)
        

# genC = cube_generator([1,2,3,4,5])
# print(next(genC))
# print(next(genC))
# print(next(genC))
# print(next(genC))
# print(next(genC))

# for num in genC:
#     print(num)


def SimpleGenerator():
    # This will execute at first call
    yield "First Yield"

    # This will execute at second call
    yield "Second Yield"

    # This will execute at Third call
    yield "Third Yield"

genC = SimpleGenerator()
for i in SimpleGenerator():
    print(i)