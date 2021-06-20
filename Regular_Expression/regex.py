import re

text = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
bla blabla

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

example.com
321-555-40
123.555.1234
123*555*1234
600-555-1234
700-555-1234
800-555-1234
900-555-1234

Mr. Abc 122
Mr Xyz
Ms Pqqr
Mrs. Lmno
Mr. Z
Mr. abc
Mr. dfgb
'''

# pattern = re.compile(r'[6789]00[-.*]\d{3}[-.*]\d{1,4}')

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

for iter in pattern.finditer(text):
    print(iter)

# # \t - Tab
# # \n - newline
# # \b - backspace
# print(r'bla\b')

# pattern = re.compile(r'[69]00[.*-]\d\d\d[.*-]\d\d\d\d')

# text_line = "Python Pynthon is+ great [ language and it is 100 like an 567 ocean, a jug can not be filled as a full knowledge from this ocean "

# pattern = re.compile(r'[0-9]{2}')

# pattern = re.compile(r'[^a-zA-Z0-9]')

# pattern = re.compile(r'\d{3}[.*-]\d{3}[.*-]\d{1,4}')

# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')


# print(pattern.findall('Python is great [ language and it is like an ocean, a jug can not be filled as a full knowledge from this ocean '))

# [] - represents a character class
# ^ - beginning of the string will be matched / matches the beginning
# $ - matches the end but not newline character
# . - matches any character except newline
# ? - matches zero or more occurrence
# * - any number of occurrence
# + - one or more occurrence
# {} - indicate number of occurrence of preceding regular expression to match
# () - enclose the group of regular expression
# \ - used to drop the special meaning of the character
# | - matches with any of the characters


# \d - matches any decimal digit which is equivalent to [0-9]
# \D - matches any non-digit character
# \s - matches whitespace character
# \S - matches non-whitespace character
# \w - matches any alphanumeric character. which is equivalent to [a-zA-Z0-9]
# \W - matches any non-alphanumeric character
# \b - Word boundry
# \B - not a word boundry