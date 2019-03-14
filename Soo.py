import os
import requests
from lxml import etree
from bs4 import BeautifulSoup as bs

class Soo():
    def __init__(self):
        self.__headers = {
            'User-Agent': "Mozilla/5.0(Windows NT 6.1;WOW64) AppleWebKit/5377.1 \
            (KHTML,like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

    def request(self,url):
        content = requests.get(url,self.__headers)
        return content

    def start_url(self,url):
        page_url = bs(self.request(url).text,'lxml').find('li',class_='btn btn-primary next').find('a')['href'][:-2]
        for pageNum in range(1,24):
            page_urls = page_url + str(pageNum)
            # self.get_content(page_urls)

#//*[@id="index"]/article/a/@href

soo = Soo()
soo.start_url(url="https://www.soo9s.com")