#! python3

import re

# Regex that matches a number with commas for every three digits
commaRegex = re.compile(r'^\d{1,3}(,\d{3})*$')

mo = commaRegex.search('1,234')

print('The number has been found ' + str(mo))

# Regex that matches the fullname of someone whose last name is Nakamoto
nameRegex = re.compile(r'^\w[A-Z][a-z]*\sNakamoto')

# mo2 = nameRegex.findall('Alice')

print('The name ' + str(mo2) + ' has been found')

# Regex that matches a sentence where the first word is group 1, second word is group 2, and third word is group 3; it is also case-insensitive
sentRegex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseball)\.', re.IGNORECASE)
