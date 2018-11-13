#!/usr/bin/python3

word = "test"
l = [word[0]]

reverse = False

while len(l) != 0:
    print(''.join(l))
    if len(l) == len(word):
        reverse = True
    if reverse:
        l.pop()
    else:
        l.append(word[len(l)])
