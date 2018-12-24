import requests,sys,re, os,shutil
from bs4 import BeautifulSoup as bs


def saveImages(BSoup,url):
    for p in BSoup.findAll('img'):
        print("Downloading {}...".format(p['src'].split('/')[-1]))
        p['src'] = p['src'][1:] #remove . that i put into plain html
        os.makedirs("site"+'/'.join(p['src'].split('/')[:-1]))
        with open("site"+p['src'],'wb') as f:
            for chunk in requests.get(url+p['src'],stream=True).iter_content(2048):
                f.write(chunk)

def saveLinks(BSoup):
    for l in BSoup.findAll('a'):
        print(l)
        # with open("site/")
        #     requests.get(l['href']).text.replace('src="','src=".')





def main():
    reg = re.compile("(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})")
    ar = sys.argv
    if len(ar)<2 or len(ar)>2:
        print("Please provide url as argument")
        return
    if not reg.match(ar[1]):
        print("Wrong url")
        return
    if not ar[1].startswith("http"):
        ar[1] = "http://"+ar[1]

    try:
        os.mkdir("site")
    except FileExistsError:
        print("Folder 'site' is already in directory. Do you want to delete it?")
        if str(input("(y/n)\n")).lower()!='y':
            return
        print("Deleting folder 'site'!...")
        shutil.rmtree("./site")
        print("Making new folder site")
        os.mkdir("site")

    r = requests.get(ar[1])
    sr = r.text
    sr = sr.replace('src="','src=".')
    with open("site/index.html","w") as f:
        f.write(sr)
    b = bs(sr,'html.parser')

    saveImages(b,ar[1])
    #TODO:
    # saveLinks(b)






if __name__ == "__main__":
    main()