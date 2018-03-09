def isPhoneNumber(text):
    if len(text)!=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if not text[3]=='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if not text[7]=='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
print('415-555-4242 is a phone number:',end='')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:',end='')
print(isPhoneNumber('Moshi moshi'))