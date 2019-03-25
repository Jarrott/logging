from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

first_url = 'http://www.cbrc.gov.cn/chinese/newIndex.html'
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (X11; Linux x86_64) \
    AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"')
browser = webdriver.Chrome(chrome_options=options)
browser.get(first_url)
html = browser.page_source
print(html)
