import sys
message = ' '.join(sys.argv[2:])
key = int(sys.argv[1])
ciphertext = [''] * key
for c in range(key):
    currIndex = c
    while currIndex < len(message):
        ciphertext[c] += message[currIndex]
        currIndex += key
print(''.join(ciphertext))

