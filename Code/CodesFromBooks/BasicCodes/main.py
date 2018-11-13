#!/usr/bin/python3
import customModule
import customNamespace

def main():
    customModule.hey()
    print("namespaceVariable in customNamespace: " + customNamespace.namespaceVariable)
    namespaceVariable = "Hello from main.py"
    print("namespaceVariable in main: " + namespaceVariable)
    print(namespaceVariable+' '+customNamespace.namespaceVariable)

if __name__ == "__main__":
    main()