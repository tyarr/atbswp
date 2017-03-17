import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

mo = phoneNumRegex.search('My number is 415-444-2353')

print('The number has been found ' + mo.group())