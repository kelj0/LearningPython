#!/usr/bin/python3
import pyautogui,time

i=5
while i>0:
    print('Drawing starts in %ss' %(i))
    time.sleep(1)
    i-=1

pyautogui.click()
distance = 200
while distance>0:
    pyautogui.dragRel(distance,0)
    distance-=5
    pyautogui.dragRel(0,distance)
    pyautogui.dragRel(-distance,0)
    distance-=5
    pyautogui.dragRel(0,-distance)
