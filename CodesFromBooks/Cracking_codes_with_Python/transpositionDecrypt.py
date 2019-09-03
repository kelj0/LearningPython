import sys,math
msg = ' '.join(sys.argv[2:])
key = sys.argv[1]
result = ''
for k in range(int(math.ceil(len(msg)/float(key)))):
    result += msg[k::int(key)+1]
print(result)

