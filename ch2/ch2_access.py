#Chapter 2 Code
print ('What is your name?')
name = input()
if name == 'Mary':
    print('Hello Mary')
else:
    print('Stop hacking! Leave now ' + str(name))
print ('What is your password?')
password = input()
if password == 'swordfish' and name == 'Mary':
    print('Access Granted!')
else:
    print('Access Denied!!!!')

