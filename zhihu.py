import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException 

url="https://www.zhihu.com/signin"
brower = webdriver.Chrome()
brower.get(url)
try:
    element = brower.find_element_by_name("username")
    element.send_keys("15521102069")
    time.sleep(3)
    pwd_element = brower.find_element_by_name("password")
    pwd_element.send_keys("bin1995." + Keys.ENTER)
    print(brower.page_source)
except ElementNotVisibleException as e:
    print(e)
    brower.close()