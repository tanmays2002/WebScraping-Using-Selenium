from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/91735/OneDrive/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://www.ajio.com/search/?text=bag%20pack')

old_height = driver.execute_script('return document.body.scrollHeight')

counter = 1
while True:

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == old_height:
        break
    old_height = new_height


html = driver.page_source
with open('ajio.html','w',encoding='utf-8') as f:
    f.write(html)