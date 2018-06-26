#!/usr/bin/python3
#Given a string, return a version without the first and last char, 
# so "Hello" yields "ell". The string length will be at least 2.


def without_end(str):
    a=len(str)-1
    a=int(a)
    return str[1:a]

without_end('Hello') 
without_end('java')
without_end('coding')