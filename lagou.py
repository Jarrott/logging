import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url ="https://www.lagou.com/jobs/list_php?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput="
brower = webdriver.Chrome()
brower.get(url)

content = bs(brower.page_source,'html.parser').find('div',class_='s_position_list').find_all('li')
print(content)
# for position_list in content:
#     print(position_list)


