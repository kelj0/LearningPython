import requests
from bs4 import BeautifulSoup

URL = "http://index.page.com/index"
req = requests.get(URL)
soup = BeautifulSoup(req.text,"html.parser")
PATH = "/path/to/download/folder"
for link in soup.find_all('a')[8:]:
    songUrl = URL+link['href']
    songName = link['href'].replace('%','_')
    r = requests.get(songUrl,stream=True)
    print("Downloading "+songName)
    with open(PATH+songName,'wb') as f:
        for chunk in r.iter_content(chunk_size=4096): 
            if chunk:
                f.write(chunk)
    print("Done!")
