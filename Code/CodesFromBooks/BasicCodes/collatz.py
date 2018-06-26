#!/usr/bin/python3
def collatz(number):
    if number%2==0:
        print(number//2)
        number=number//2
    elif number==1:
        return number
    else:
        print(3*number+1)
        number=3*number+1
    collatz(number)


enter=input("Enter number:")
enter=int(enter)
collatz(enter)
