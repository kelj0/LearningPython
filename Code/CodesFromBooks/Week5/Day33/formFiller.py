# formFiller.py Automatically fills in the form

import pyautogui,time

nameField = (564,345)
submitButton = (533,870)
submitButtonColor = (72,137,241)
submitAnotherButton=(649,255)

formData = [{'name':'Karlo','fear':'Not going to Angerfist','source':'wand',
            'robocop':4,'comments':'No comment'},
            {'name':'Rok','fear':'Not going to Angerfist','source':'crystal ball',
            'robocop':4,'comments':'No comment'},
            {'name':'Tomo','fear':'Matematix plox','source':'money',
            'robocop':4,'comments':'ne znam ja nista ja sam sa krka'}]

pyautogui.PAUSE = 0.5 # Wait 0.5s after every pyautogui foo
for person in formData:
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)
    while not pyautogui.pixelMatchesColor(submitButton[0],submitButton[1],submitButtonColor):
        time.sleep(0.5)
    print('Entering %s info...' % (person['name']))
    pyautogui.click(nameField[0],nameField[1])
    pyautogui.typewrite(person['name']+'\t')
    pyautogui.typewrite(person['fear']+'\t')
    
    if person['source']=='wand':
        pyautogui.typewrite(['down','\t'])
    elif person['source']=='amulet':
        pyautogui.typewrite(['down','down','\t'])
    elif person['source']=='crystal ball':
        pyautogui.typewrite(['down','down','down','\t'])
    elif person['source']=='money':
        pyautogui.typewrite(['down','down','down','down','\t'])

    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])
    
    pyautogui.typewrite(person['comments'])

    pyautogui.moveTo((533,870))
    pyautogui.click()
    print('Clicked Submit.')
    time.sleep(5)
    pyautogui.click(submitAnotherButton[0],submitAnotherButton[1])
