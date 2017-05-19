import re

while True:
    print('Select a secure password. 8 characters in length, 1 uppercase, 1 lower case, 1 numeral')
    password = input()
    if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        print('Very nice password. Much secure')
        break
    else:
        print('Not a valid password')