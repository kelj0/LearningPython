#! /usr/bin/python3

import sys,os,argparse
from termcolor import colored

def noArg():
    return '\n'.join(sorted([f for f in os.listdir(os.getcwd()) if not f.startswith('.')]))

def listAll():
    return '\n'.join(sorted([f for f in os.listdir(os.getcwd())]))

def listColor():
    return '\n'.join([colored(f,'cyan') if os.path.isdir(f) else f for f in os.listdir(os.getcwd())])
    
def noBackup():
	return '\n'.join([colored(f,'cyan') if os.path.isdir(f) and !f.endswith('~') else f for f in os.listdir(os.getcwd())])

def main():
    parser = argparse.ArgumentParser(description="ls like command implemented in python")
    parser.add_argument('-a',help="Lists all files in current dir.",dest="listAll",action="store_true")
    parser.add_argument('--color',help="Lists all files in current dir.(colored)",dest="listColor",action="store_true")
	parser.add_argument('-B',help="List all files, do not list implied entries ending with ~",dest="noBackup",action="store_true")

    if len(sys.argv) == 1:
        print(noArg())
    else:
        parsed = parser.parse_args()
        if parsed.listAll:
            print(listAll())
        elif parsed.listColor:
            print(listColor())


if __name__ == '__main__':
    main()

