#! python3
# Program to check if password matches requirements

import re

# Function & Regex
strongPassword = re.compile(r'^(?=.*[A-Z].*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z].*[a-z].*[a-z]).{8}$')

# input text
password = input()

# check against regex req.
matches = []
for groups in strongPassword.findall(text):
    (groups[0])  #

#while True:
#    print('Select a password (8 characters, 2 uppercase, 1 special, 2 numerals, 3 lower')
#    password = input()
#    if password is strongPassword.search(input()):
#        break
#    print('That is not a valid password')


