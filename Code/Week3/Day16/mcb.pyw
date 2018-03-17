#mcb.pyw - Saves and loads pieces of text to the clipboard
# USAGE: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcb.pyw <keyword> -Loads keyword to clipboard
#        py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve,pyperclip,sys

mcbShelf = shelve.open('mcb')

if len(sys.argv)==3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print("Succesfully saved clipboard contet under key {}".format(sys.argv[2]))
elif len(sys.argv)==3 and sys.argv[1].lower()=='delete':
    try:
        del mcbShelf[sys.argv[2]]
        print("Deleted ",sys.argv[2])
    except KeyError:
        print("Sorry there is no item called like that..il print you available")
        for key in mcbShelf.keys():
            print(key)
elif len(sys.argv) == 2:
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        for key in mcbShelf.keys():
            print(key)
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print("Contet from {} copyed to clipboard".format(sys.argv[1]))

mcbShelf.close()