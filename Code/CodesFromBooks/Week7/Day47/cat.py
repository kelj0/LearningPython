#!/usr/bin/python3

import sys
# cat.py -f file [> file] [-n 5] 

hlp = """Desc: Read files,copy content of files..
    Usage: -f 'filename' , [optional number of rows] -n 5
    You can use > to append 1 file content to another
    (-f file1.txt > file2.txt)
    -also you can combine with -n of lines to copy"""

if sys.argv[1]=='-h':
    print(hlp)
elif len(sys.argv)==1:
    print("Please provide arguments!")
elif len(sys.argv)==3:
    try:
        f = open(sys.argv[2])
    except FileNotFoundError as er:
        print("File doesnt exist!\nError:",er)
    print(f.read())
    f.close()
elif sys.argv[3]=='>':
    if sys.argv[5]=='-n':
        print("a")
        try:
            f = open(sys.argv[2],'r')
            out = open(sys.argv[4],'a')
        except FileNotFoundError as er:
            print("File doesnt exist!\nError:",er)
        for i in range(int(sys.argv[6])):
            out.write(f.readline())
        f.close()
        out.close()
    else:
        try:
            f = open(sys.argv[2],'r')
            out = open(sys.argv[4],'a')
        except FileNotFoundError as er:
            print("File doesnt exist!\nError:",er)
        out.write(f.read())
        f.close()
        out.close()
elif sys.argv[3]=='-n':
    try:
        f = open(sys.argv[2])
    except FileNotFoundError as er:
        print("File doesnt exist!\nError:",er)
    for i in range(int(sys.argv[4])):
        print(f.readline(),end="")
    f.close()
else:
    print(hlp)
