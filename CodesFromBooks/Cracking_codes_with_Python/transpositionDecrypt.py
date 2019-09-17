import sys,math

def main():
    msg = ' '.join(sys.argv[2:])
    key = int(sys.argv[1])
    print(transpositionDecrypt(msg,key))

def transpositionDecrypt(msg,key):
    columns = int(math.ceil(len(msg)/float(key)))
    shadedRows = columns*key - len(msg)
    result = ['']*columns
    currR = 0
    currC = 0
    for k in msg:
        result[currC] += k
        currC+=1
        if currC == columns or (currC == columns-1 and currR >= key-shadedRows):
            currC = 0
            currR += 1
    return ''.join(result)

if __name__ == '__main__':
    main()
