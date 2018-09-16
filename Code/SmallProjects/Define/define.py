#! /usr/bin/python3

import requests,json,sys,os,pyperclip,re,keyboard

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

word = "test"

def main():
    global word
    print("Starting script... press 'ctrl+space' to turn off")
    while not keyboard.is_pressed('ctrl+space'):
        if pyperclip.paste() != word and len(pyperclip.paste().split())<3:
            word = pyperclip.paste()
            wordChc=False
            req = requests.get("https://api-portal.dictionary.com/dcom/pageData/%s" % word)
            wordChcURB = False
            reqURB=requests.get('https://api.urbandictionary.com/v0/define?term=%s' % word)
            try:    
                data = json.loads(req.text)['data']['content'][0]['entries'][0]['posBlocks'][0]['definitions']
            except TypeError:
                os.system('notify-send "Cant find |%s| on dictionary.com!"' % word)
                wordChc = True
            except KeyError:
                os.system('notify-send "Cant find |%s| on dictionary.com!"' % word)
                wordChc = True

            if not wordChc:
                definitions = []
                for definition in data[:3]:
                    definitions.append(cleanhtml(definition['definition']))
                    definitions.append("------------")
                os.system('notify-send "definitions from dictionary.com:[{}\n{}"'\
                .format(word+"]\n------------",'\n'.join(definitions)))
            
            try:    
                dataURB = json.loads(reqURB.text)['list']
            except TypeError:
                os.system('notify-send "Cant find |%s| on urbandictionary.com!"' % word)
                wordChcURB = True
            except KeyError:
                os.system('notify-send "Cant find |%s| on urbandictionary.com!"' % word)
                wordChcURB = True

            if not wordChcURB:    
                definitionsURB = []
                for definition in dataURB[:3]:
                    definitionsURB.append(definition['definition'])
                    definitionsURB.append("------------")
                os.system('notify-send "definitions from urbandictionary.com:[{}\n{}"'\
                .format(word+"]\n------------",'\n'.join(definitionsURB)))
    os.system('notify-send "Thank you for using define.py made by kkeglje"')


if __name__ == '__main__':
    main()