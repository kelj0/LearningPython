import sys


def transpositionEncrypt(message,key):
    ciphertext = [''] * key
    for c in range(key):
        currIndex = c
        while currIndex < len(message):
            ciphertext[c] += message[currIndex]
            currIndex += key
    return ''.join(ciphertext)

def main():
    message = ' '.join(sys.argv[2:])
    key = int(sys.argv[1])
    print(transpositionEncrypt(message,key))

if __name__ == '__main__':
    main()
