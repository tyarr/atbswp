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
    (groups[0])


