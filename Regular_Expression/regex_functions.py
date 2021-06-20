import re

text_line = "Python is great language and it is like an ocean, a jug can not be filled as a full knowledge from this ocean "

# # sub()
# print(re.sub('\s', '#', text_line, 4))

# # split()
# print(re.split('\s', text_line, 2))

# # search()
# print(re.search('OCEAN', text_line, re.IGNORECASE))

# # match()
# print(re.match('Python is GREAT', text_line, re.IGNORECASE))

# # findall()
pattern = re.compile(r'[a-zA-Z]+')
# print(pattern.findall(text_line))

for iter in pattern.findall(text_line):
    print(iter)