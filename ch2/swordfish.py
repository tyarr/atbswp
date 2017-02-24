while True:
    print('What is your username?')
    name = input()
    if name != 'Tyler':
        continue
    print('Hello Tyler, what is your password')
    password = input()
    if password == 'swordfish':
        break
    else:
        print('stop hacking!')
print('Access Granted!')
    
