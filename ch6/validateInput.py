while True:
    print('Enter your age')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age')

while True:
    print('Select a password (letters and numbers only)')
    password = input()
    if password.isalnum():
        break
    print('That is not a valid password')
