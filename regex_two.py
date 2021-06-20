import re

emails = '''
abcXYZ@gmail.com
abc.xyz@pqr.org
abc-123-XYZ@any-mail.net
abc-123-XYZ@way2sms.edu
abc_XYZ@way2sms.ai
'''

urls = '''
https://facebook.com
https://www.youtube.com
http://www.google.com
http://www.india.gov
https://ww3.instagram.com
'''

# # for emails
# pattern = re.compile(r'[a-zA-Z0-9.-_]+@[a-zA-Z0-9-]+\.[a-zA-Z]+')

pattern = re.compile(r'https?://(ww(w|[0-9]?)\.)?(\w+)(\.\w+)')

for iter in pattern.finditer(urls):
    print(iter)
