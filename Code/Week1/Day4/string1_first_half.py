#Given a string of even length,
#return the first half. So the string "WooHoo" yields "Woo".

def first_half(str):
    a=len(str)/2
    a=int(a)
    return str[0:a]

first_half('WooHoo')
first_half('HelloThere')
first_half('abcdef')