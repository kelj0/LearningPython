import requests,sys,re,os,shutil
from bs4 import BeautifulSoup as bs


srcPattern = re.compile('(?<=src=(\'|\"))(.*?)(?=\s*(\'|\"))')
hrefPattern = re.compile('(?<=href=(\'|\"))(.*?)(?=\s*(\'|\"))')
ahrefPattern = re.compile('(?<=a href=(\'|\"))(.*?)(?=\s*(\'|\"))')


def saveImages(BSoup,l):
    for p in BSoup.findAll('img')[:2]:
        print("[Downloading image] {}...".format(p['src'].split('/')[-1]))
        try:
            with open("site/images/"+p['src'].split('/')[-1],'wb') as f:
                try:
                    for chunk in requests.get(p['src'],stream=True).iter_content(1024):
                        f.write(chunk)
                except requests.exceptions.MissingSchema:
                    for chunk in requests.get(l+p['src'],stream=True).iter_content(1024):
                        f.write(chunk)
        except IsADirectoryError:
            print("no src in img..skipping")
            continue

def saveJS(BSoup,l):
    for js in BSoup.findAll('script'):
        try:
            with open('site/script/'+js['src'].split('/')[-1],'w') as f:
                f.write(requests.get(js['src']).text)
            print("Found js include, extracting js code and writing it to " + js['src'].split('/')[-1])
        except TypeError:
            print("Found inner js, im not download it")
        except KeyError:
            print("Found inner js, im not download it")
        except requests.exceptions.MissingSchema:
            with open('site/style/'+js['src'].split('/')[-1],'w') as f:
                f.write(requests.get(l+js['src']).text)

def saveCSS(BSoup,l):
    for css in BSoup.findAll(attrs={'rel':'stylesheet'}):
        try:
            with open('site/style/'+css['href'].split('/')[-1],'w') as f:
                f.write(requests.get(css['href']).text)
            print("Found css include, extracting css and writing it to " + css['href'].split('/')[-1])
        except KeyError:
            print("Found inner css, im not download it")
        except TypeError:
            print("Found inner css, im not download it")
        except requests.exceptions.MissingSchema:
            with open('site/style/'+css['href'].split('/')[-1],'w') as f:
                f.write(requests.get(l+css['href']).text)

def downloadHtml(link,name):
    r = requests.get(link).text
    saveImages(bs(r,'html.parser'),link)
    saveJS(bs(r,'html.parser'),link)
    saveCSS(bs(r,'html.parser'),link)
    src = srcPattern.findall(r)
    href = hrefPattern.findall(r)
    ahref = ahrefPattern.findall(r)
    for s in src:
        print("Adjusting src: " + s[1].split('/')[-1])
        if not (s[1][-3:]=='css' or s[1][-2:] == 'js'):
            r = r.replace(s[1],'images/'+s[1].split('/')[-1],1)
        elif s[1][-3:]=='css':
            r = r.replace(s[1],'style/'+s[1].split('/')[-1],1)
        else:
            r = r.replace(s[1],'script/'+s[1].split('/')[-1],1)
    for s in href:
        print("Adjusting href: " + s[1])
        if not (s[1][-3:]=='css' or s[1][-2:] == 'js'):
            r = r.replace(s[1],'images/'+s[1].split('/')[-1],1)
        elif s[1][-3:]=='css':
            r = r.replace(s[1],'style/'+s[1].split('/')[-1],1)
        else:
            r = r.replace(s[1],'script/'+s[1].split('/')[-1],1)
    for s in ahref:
        print("Adjusting href: " + s[1])
        try:  #ok
            if len(s[1].split('/')[-1])<1:
                r = r.replace(s[1], s[1].split('/')[-2],1)
            elif len(s[1].split('/')[-1])==1:
                continue
            else:
                r = r.replace(s[1], s[1].split('/')[-1],1)
        except IndexError:
            print("Empty link")

    with open("site/"+name+'.html',"w") as f:
        f.write(r)


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
        os.mkdir("site/images")
        os.mkdir("site/style")
        os.mkdir("site/script")
    except FileExistsError:
        print("Folder 'site' is already in directory. Do you want to delete it?")
        if str(input("(y/n) ")).lower()!='y':
            return
        print("Deleting folder 'site'!...")
        shutil.rmtree("./site")
        print("Making new folder site")
        os.mkdir("site")
        os.mkdir("site/images")
        os.mkdir("site/style")
        os.mkdir("site/script")
    
    downloadHtml(ar[1],'index')
    l = bs(requests.get(ar[1]).text,'html.parser').findAll('a')
    for c,link in enumerate(l):
        try:
            print("\n-----\n[{}/{}]".format(c,len(l)))
            print("---------------------\nFound new link! [{}] downloading html..\n---------------------".format(link['href']))
            downloadHtml(link['href'],link['href'].split('/')[-1])
        except requests.exceptions.MissingSchema:
            downloadHtml(ar[1]+link['href'],link['href'].split('/')[-1])
        except KeyError:
            print(link)
    


if __name__ == "__main__":
    main()

    print("Done!")