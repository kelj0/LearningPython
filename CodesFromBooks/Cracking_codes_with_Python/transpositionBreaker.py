from transpositionDecrypt import transpositionDecrypt
import sys

msg = ' '.join(sys.argv[1:])

print("[i] Checking keys 0-25")
for i in range(1,26):
    print("[Key {0}] -> {1}".format(i,transpositionDecrypt(msg,i)))

