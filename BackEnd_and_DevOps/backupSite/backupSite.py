import requests,sys,re
from bs4 import BeautifulSoup as bs



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
    r = requests.get(ar[1])
    with open("test.html","w") as f:
        f.write(r.text)
    #b = bs(r.text,'html.parser')
    #TODO: download pictures, and all sites linked on site





if __name__ == "__main__":
    main()