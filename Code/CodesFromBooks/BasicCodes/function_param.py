#!/usr/bin/python3
def print_max(a,b):
    a=a+1
    if a>b:
        print("a is maximum")
    elif a==b:
        print("a is equal to b")
    else:
        print("b is maximum")
    print("In function",a)

a=10
b=10

print_max(a,b)
print("After function",a)