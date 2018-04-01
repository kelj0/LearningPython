# 2048.py script automaticly plays game 2048

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


browser = webdriver.Firefox()

browser.get('https://gabrielecirulli.github.io/2048/')

linkKey = browser.find_element_by_tag_name('html')

retry = browser.find_element_by_class_name('retry-button')
while True:
    
    linkKey.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.01)
    linkKey.send_keys(Keys.ARROW_LEFT)
    time.sleep(0.01)
    linkKey.send_keys(Keys.ARROW_UP)
    time.sleep(0.05)
    linkKey.send_keys(Keys.ARROW_RIGHT)
    time.sleep(0.05)
    
    try:
        gameOver = browser.find_element_by_class_name('game-over')
        if gameOver:
            time.sleep(10)
            retry.click()
    except NoSuchElementException:
        print('Playing...')
        



    
    
