#! /usr/bin/python3

import os, json
from flask import Flask

app = Flask(__name__)



def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
    return d


@app.route("/")
def getFiles():
	return json.dumps(path_to_dict('.'),indent=2,sort_keys=True)     



def main():
    print("Starting server...")
    app.secret_key = "testing"
    app.run(host='0.0.0.0',debug=True)


if __name__=='__main__':
    main()

