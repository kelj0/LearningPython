# 2048.py script automaticly plays game 2048


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://gabrielecirulli.github.io/2048/')

linkKey = browser.find_element_by_tag_name('html')
browser.close()
retry = browser.find_element_by_class_name('retry-button')
while True:
    linkKey.send_keys(Keys.ARROW_DOWN)
    browser.implicitly_wait(1)
    linkKey.send_keys(Keys.ARROW_LEFT)
    browser.implicitly_wait(1)
    linkKey.send_keys(Keys.ARROW_UP)
    browser.implicitly_wait(1)
    linkKey.send_keys(Keys.ARROW_RIGHT)
    browser.implicitly_wait(1)
    try:
        retry.click()
    except Exception:
        print('Playing...')
        



    
    
