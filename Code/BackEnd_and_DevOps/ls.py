#! /usr/bin/python3

import sys,os,argparse

def noArg():
    return '\n'.join(sorted([f for f in os.listdir(os.getcwd()) if not f.startswith('.')]))

def listAll():
    return '\n'.join(sorted([f for f in os.listdir(os.getcwd())]))

def main():
    parser = argparse.ArgumentParser(description="ls like command implemented in python")
    parser.add_argument('-a',help="Lists all files in current dir.",dest="listAll",action="store_true")
    if len(sys.argv) == 1:
        print(noArg())
    else:
        parsed = parser.parse_args()
        if parsed.listAll:
            print(listAll())


if __name__ == '__main__':
    main()

