def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text==text[::-1]

somenthing=input('Enter word:')

if is_palindrome(somenthing):
    print('Yes, it is palindrome')
else:
    print('No, it is not a palindrome')
