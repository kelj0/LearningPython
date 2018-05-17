#!/usr/bin/python3
import shutil,os

print("Start")
rootDir = '..'
for dirName, subdirList, fileList in os.walk(rootDir):
    print("Files are changed in %s" % dirName)
    for fname in fileList:
        if not (str(fname).startswith("settings") or str(fname).startswith("_"))and str(fname).endswith(".py") :
            from_file = open(dirName+r'/'+fname)
            line = from_file.readline()
            line = "#!/usr/bin/python3\n"+line
            to_file = open(dirName+r'/'+fname,mode="w")
            to_file.write(line)
            shutil.copyfileobj(from_file,to_file)
            from_file.close()
            to_file.close()
            print(fname)
    print("Done with %s" % dirName)
print("Done")