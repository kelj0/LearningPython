#!/usr/bin/python3
import re

def isPhoneNumber(text):
    check= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo= check.search(text)
    print("TESTS:",mo,mo.group(),str(mo.group()),sep="|||")
    if len(str(mo.group))>1:
        return mo.group()
    else:
        return "Number not found"
print('Number is: '+ isPhoneNumber("Tel number is 123-123-1234"))