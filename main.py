from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
# import pyperclip
# import time
# import sys
from time import sleep
from selenium.webdriver.common.keys import Keys

from config import CHROME_PROFILE_PATH



options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)
browser = webdriver.Chrome(executable_path='C:\chromedriver/chromedriver', options=options)
browser.maximize_window()
browser.get('https://tinder.com')
   
    
    # sleep(200000)
sleep(1)
try:
         sleep(2)
         login = browser.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
    
         login.click()
         fb_login = browser.find_element('xpath', '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div')
         fb_login.click()
except:
        
        
 while True:
    number = random.randint (0,1)
    print (number)   
    sleep(2)
    if number == 1:
            track = browser.find_element('xpath', '//*[@id="Tinder"]/body')
            track.send_keys(Keys.ARROW_RIGHT)
    elif number == 0:
            track = browser.find_element('xpath', '//*[@id="Tinder"]/body')
            track.send_keys(Keys.ARROW_LEFT)





