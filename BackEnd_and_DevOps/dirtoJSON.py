import sys, os, json, pprint

_json = {}

def getFiles(path,fold="./"):
    global _json
    for f in os.listdir(path):
        if os.path.isdir(f):
            _json[f] = []
            print("Found new dir: " + f)
            getFiles(path+'/'+f,f)
        else:
            print("Appending files in directory: " + fold)
            if fold in _json:
                _json[fold].append(f)
            else:
                _json[fold] = [f]
                
def main():
    getFiles(os.getcwd())
    pprint.pprint(_json)


if __name__=='__main__':
    main()

