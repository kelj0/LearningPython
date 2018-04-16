def copyFile(inFile,outFile):
    inf = open(inFile,"r")
    out = open(outFile,"w")
    count = 0
    line = inf.readline()
    while line !="":
        count +=1
        line = inf.readline()
    inf.close()
    out.close()
    return count