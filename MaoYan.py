import os
import requests
from bs4 import BeautifulSoup as bs
from multiprocessing import pool
from requests.exceptions import RequestException

class MaoYan:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

    def request(self,url):
        try:
            response = requests.get(url,headers=self.headers)
            if response.status_code == 200:
                return response.text
        except RequestException as e:
            print('error:',e)
            return False
    
    def all_url(self,first_url):
        for i in range(10):
            url = first_url+str(i*10)
            html = self.request(url)
            self.parse_html(html)

    def parse_html(self,html):
        content_html = bs(html,'html.parser').find('dl',class_="board-wrapper")
        print(content_html)
        
maoyan = MaoYan()
url = 'https://maoyan.com/board/4?offset='
maoyan.all_url(url)