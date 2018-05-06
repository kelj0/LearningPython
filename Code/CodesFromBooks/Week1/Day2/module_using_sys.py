import sys
import os;print(os.getcwd())

print("The command line arguments are:")
for i in sys.argv:
    print(i)

print ("\n\nThe PYTHONPATH is",sys.path,"\n")
