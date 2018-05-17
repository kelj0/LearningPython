#!/usr/bin/python3
#!/usr/bin/python3
#! python3
#pw.py - an insecure password locker program.

PASSWORDS={'email': 'aSADSAKdj9813sSA12ODd0s9ajdsa',
           'blog': 'sadalskdSADads2SAD2d3413421DSA',
           'luggage': '12345'}

import sys,pyperclip
if len(sys.argv)<2:
    print ('Usage: py pw.py [account] -copy account password')
    sys.exit()

account = sys.argv[1] #first command line arg is account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
