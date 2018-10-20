# Scrapes songs from bandcamp

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

gecPATH = "/full/path/to/geckodriver"
browser = webdriver.Firefox(executable_path=gecPATH)
site = "https://bandcamp.com/EmbeddedPlayer" # find player
browser.get(site)
PATH = "path/to/save/"
browser.find_element_by_class_name('tracktitle').click() # click on first song
for i in range(??): # Put here number of songs in embedded player
    browser.find_element_by_id("big_play_button").click()
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    songLink = soup.findAll("audio")[0]['src']
    songName = soup.select('span[id="currenttitle_title"]')\
                [0].getText().replace(' ','_')
    print("Downloading "+songName + "...\n")
    r = requests.get(songLink,stream=True)
    with open(PATH+songName+".mp3",'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    browser.find_element_by_id('next').click()
