#!/usr/bin/python3
# Extract emails from txt file , just replace file.txt to yourfilename.txt :)
# Also if you want to write it to file replace print(e.group())[line 12] to something like file.write...
import re

emails = open("file.txt","r")
emailList = []
emails.readline()
for line in emails:
    emailList.append(re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Za-z]{2,6}\b',line))
for e in emailList:
    try:
        print(e.group())
    except AttributeError:
        continue
emails.close()
