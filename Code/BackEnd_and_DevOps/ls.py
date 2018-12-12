#! /usr/bin/python3

import sys,os


def noArg():
    return '\n'.join([f for f in os.listdir(os.getcwd())])

def help():
    return "Wrong args!\nUsage:\n-te\n-tes\n-test"""

def main():
    if len(sys.argv) == 1:
        print(noArg())
    else:
        print(help())
    
    
if __name__ == '__main__':
    main()

