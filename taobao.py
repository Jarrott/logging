import re
import time
import pymongo
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq

brower = webdriver.Chrome()
wait = WebDriverWait(brower,10)
try:
    brower.get('https://www.taobao.com')
    input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#q'))
    )
    input.send_keys('零食')
    submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button'))
    )
    submit.click()
    total = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total'))
    )
    print(total)
except Exception as e:
    print(e)

brower.close()

