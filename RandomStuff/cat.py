#!/usr/bin/python3

import sys
# cat.py file [toFile] [-n 5] 


#Make description and print it if bad args
hlp = """Desc: Read files,copy content of files..
    Usage: python cat.py 'filename' , ([optional number of rows] -n 5)
    You can append 1 file content to another
    (python cat.py file1.txt file2.txt)
    You can also combine with -n of lines to copy
    (python cat.py file1.txt file2.txt -n 5)
    """


def openFileR(fileName):
    """Returns TextIOWrapper(return open(f.txt,'r'))"""
    try:
        return open(fileName,'r')
    except:
        print("Cant open file!")


def openFileW(fileName):
    """Returns TextIOWrapper(return open(f.txt,'w'))"""
    try:
        return open(fileName,'w')
    except:
        print("Cant open file!")


# writing from file to file
def writeFiletoFile(readFile,writeFile):
    """writeFiletoFile(fromFile,toFile),writes content of fromFile to toFile"""
    fromFile = openFileR(readFile)
    toFile = openFileW(writeFile)

    toFile.write(fromFile.read())

    fromFile.close()
    toFile.close()


# write n lines from file to file
def write_N_lines(readFile,writeFile,n):
    """(fromFile,toFile,NumberOfLinesToWrite),writes n lines of content fromFile > toFile"""
    fromFile = openFileR(readFile)
    toFile = open(writeFile,'a')
    for i in range(n):
        toFile.write(fromFile.readline())

    fromFile.close()
    toFile.close()

#TODO: append to file


#TODO: write reversed content of file to file ('tac') 
# <out.writelines(reversed(f.readlines()))>


def main():    
    try:
        if len(sys.argv)==2:
            if sys.argv[1] == '-h':
                print(hlp)
            else:
                f = openFileR(sys.argv[1])
                print(f.read())
                f.close()
        else:
            if len(sys.argv)==3:
                writeFiletoFile(sys.argv[1],sys.argv[2])
            elif sys.argv[3] == '-n':
                write_N_lines(sys.argv[1],sys.argv[2],int(sys.argv[4]))
            
    except Exception as e:
        print("Bad use of cat!\n",e,"\n------------------\n",hlp)
    

if __name__ == "__main__":
    main()

