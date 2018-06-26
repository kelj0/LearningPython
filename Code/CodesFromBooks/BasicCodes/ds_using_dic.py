#!/usr/bin/python3
ab={
    'Karlo':'kegljevickarlo@gmail.com',
    'jedan':'jedanmail',
    'nisa':'nisan',
    'spam':'saldasd@ls'
}

print("Karlo adress is",ab['Karlo'])

del ab['spam']

print("There are {} contats in my dictionary".format(len(ab)))

for name,adress in ab.items():
    print("Contact {} at {}".format(name,adress))

ab['Guido']='guide@gmail.com'

if 'Guido' in ab:
    print('\n Guido adress is',ab['Guido'])
