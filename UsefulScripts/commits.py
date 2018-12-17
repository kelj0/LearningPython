#!/usr/bin/python3
import requests, bs4, sys, re

def main():
    r = re.compile('(\d\d\d\d-\d\d-\d\d)$')
    if not r.match(sys.argv[2]):
        print("""Wrong usage of date!\nUsage: python3 commit.py [name] [YYYY-MM-DD]""")
        sys.exit(1)
    req = requests.get("https://github.com/{}".format(sys.argv[1]))
    bs = bs4.BeautifulSoup(req.text, features='html.parser')
    for date in bs.find_all(class_="day"):
        if date['data-date']>=str(sys.argv[2]):
            if date['data-count'] == '0': 
                print(date['data-date'],"-> no commits!")
            else:
                print(date['data-date'], "-> ",date['data-count'])
        else: continue

if __name__ == '__main__':
    main()