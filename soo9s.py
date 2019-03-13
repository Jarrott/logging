import os
import lxml
import requests
from bs4 import BeautifulSoup as bs

class Soo:

    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0(Windows NT 6.1;WOW64) AppleWebKit/5377.1 \
            (KHTML,like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

    def request(self,url):
        content = requests.get(url,self.headers)
        return content
    
    def get_url(self,start_url):
        NextPage_url = bs(self.request(start_url).text,'lxml').find('li',class_='btn btn-primary next').find('a')['href'][:-3]
        for PageNum in range(1,25):
            page_url = NextPage_url + '/' + str(PageNum)
            # path = str(PageNum)
            # self.mkdir(path)
            self.get_html(page_url) 
            

    def get_html(self,page_url):
        html = bs(self.request(page_url).text,'lxml').find('div',class_='post-card').find('meta')['content']
        self.save(html)

    def save(self,html):
        name = html[-12:-4]
        img = self.request(html)
        with open(name + '.jpg','ab') as f:
            f.write(img.content)
            print(name,'ok')

    # def mkdir(self,path):
    #     is_exists = os.path.exists(os.path.join("E:\demo",path))
    #     if not is_exists:
    #         os.makedirs(os.path.join("E:\demo",path))
    #         os.chdir(os.path.join("E:\demo",path))
    #     else:
    #         print(path,'文件夹已存在')
            
soo = Soo()
soo.get_url(start_url = 'https://www.soo9s.com/')