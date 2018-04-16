def is_palindrome(text):
    return text==text[::-1]

something=input('Enter word:')
str(something)
something=something.replace(" ","")
print(something)
if is_palindrome(something):
    print('Yes, it is palindrome')
else:
    print('No, it is not a palindrome')
