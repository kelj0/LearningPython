#! /usr/bin/python3

import requests,json,sys,os,pyperclip,re,keyboard

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

word = "a"

def main():
    global word
    print("Starting script... press 'ctrl+space' to turn off")
    while not keyboard.is_pressed('ctrl+space'):
        if pyperclip.paste() != word and len(pyperclip.paste().split())<3:
            word = pyperclip.paste()

            req = requests.get("https://api-portal.dictionary.com/dcom/pageData/%s" % word)
            try:    
                data = json.loads(req.text)['data']['content'][0]['entries'][0]['posBlocks'][0]['definitions']
            except TypeError:
                os.system('notify-send "Cant find |%s| on dictionary.com!"' % word)
                continue
            except KeyError:
                os.system('notify-send "Cant find |%s| on dictionary.com!"' % word)
                continue

            definitions = []
            for definition in data[:3]:
                definitions.append(cleanhtml(definition['definition']))
                definitions.append("------------")
            os.system('notify-send "definitions from dictionary.com:[{}\n{}"'.format(word+"]\n------------",'\n'.join(definitions)))
    os.system('notify-send "Thank you for using define.py made by kkeglje"')


if __name__ == '__main__':
    main()