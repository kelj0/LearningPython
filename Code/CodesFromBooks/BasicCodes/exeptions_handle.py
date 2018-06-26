#!/usr/bin/python3
try:
    text=input('enter something --> ')
except EOFError:
    print('Why did you do and EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered',text)