#!/usr/bin/python3
#!/usr/bin/python3
# mouseNow.py - Prints current position of mouse

import pyautogui,time,os

try:
    print('Press Ctrl+C to quit(in console)')
    while 1:
        W,H=pyautogui.position()
        posStr = '('+str(W)+', '+str(H)+')'
        print(posStr,end='')
        time.sleep(0.2)
        print('\b'*len(posStr),end='',flush=True)
except KeyboardInterrupt:
    print()
    print('Ty for using my script')