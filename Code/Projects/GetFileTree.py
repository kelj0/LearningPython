#!/usr/bin/python3
import shutil,os

print("Start")
rootDir = '..'
for dirName, subdirList, fileList in os.walk(rootDir):
    print("-",dirName)
    for subdir in subdirList:
        print("---",subdir)
        for fname in fileList:
                print("\t",fname)

print("Done")