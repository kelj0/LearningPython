import os, json


def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
    return d

def main():
    print(json.dumps(path_to_dict('.'),indent=2,sort_keys=True))


if __name__=='__main__':

    main()

