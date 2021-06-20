# Create a file
'''
Access Modes
r - "Read only"
r+ - "Read and Write"
w - "Write only"
w+ - "Write and Read"
a - "Append only"
a+ - "Append and Read"
rb  - "Binary Read"
wb  - "Binary Write"
ab  - "Binary Append"
rb+  - "Binary Read and Write"
wb+  - "Binary Write and Read"
ab+  - "Binary Append and Read"
'''

# file = open("created_file.txt","w+")
# file.write("Hi, File Handlling Program\n")
# file.write("Hi, File Handlling Program line 2\n")
# file.write("Hi, File Handlling Program line 3\n")
# file.write("Hi, File Handlling Program line 4\n")
# file.write("Hi, File Handlling Program line 5\n")
# file.write("Hi, File Handlling Program line 6\n")
# file.write("Hi, File Handlling Program line 7\n")
# file.write("Hi, File Handlling Program line 8\n")
# file.write("Hi, File Handlling Program line 9\n")
# file.seek(20)
# print(file.readlines())
# file.close()

# file = open("created_file.txt","r+")
# # print(file.read())
# # file.seek(0)
# # print(file.readline())
# # print(file.readline())
# # file.seek(0)
# # print(file.readlines())
# for line in file.readlines():
#     print(line, end='')
# file.write("Hi, File Handlling Program line 9\n")
# file.close()


# file = open("created_file.txt","r+")
# print(file.read())
# file.write("Hi, File Handlling Program line 9\n")
# file.seek(0)
# print(file.read())
# file.close()


# file = open("created_file.txt","a+")
# file.write("\nHi, File Handlling Program line 3")
# file.seek(0)
# print(file.read())
# file.close()

# with open("created_file.txt","r") as file:
#     print(file.read())


# with open("created_file.txt","w+") as file:
#     # file.write("Hi, File Handlling Program line 10")
#     file.writelines(['Hi, File Handlling Program\n', 'Hi, File Handlling Program line 2\n', 'Hi, File Handlling Program line 3\n', 'Hi, File Handlling Program line 4\n', 'Hi, File Handlling Program line 5\n', 'Hi, File Handlling Program line 6\n', 'Hi, File Handlling Program line 7\n', 'Hi, File Handlling Program line 8\n', 'Hi, File Handlling Program line 9\n'])
#     file.seek(0)
#     print(file.read())

# file = open("binary.bin", "wb")
# numList = [1, 2, 3, 4, 5]
# binaryArr = bytearray(numList)
# file.write(binaryArr)
# file.close()


file = open("binary.bin", "rb")
print(list(file.read()))
file.close()
