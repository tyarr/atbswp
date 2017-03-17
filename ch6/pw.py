#! python3
# Password Project Automate the Boring Stuff - insecure!

PASSWORDS = {'email': 'F83r2hjfhds89yht21',
             'blog': 'VijsdfmniomAio235fds' ,
             'luggage': '1234'
             }

import sys,pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg in the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)