#!/usr/bin/python3
def replace(str):
    a=str[0]
    str=str.replace(a,"*")
    new_str=a+str[1:]
    return new_str

print(replace('initialization'))