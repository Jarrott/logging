import os
import lxml 
import requests
from bs4 import BeautifulSoup as bs

class Meizi:
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0(Windows NT 6.1;WOW64) AppleWebKit/5377.1 \
            (KHTML,like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

    def request(self,url):
        content = requests.get(url,proxies={'http':"www.mzitu.com"},headers = self.headers)
        return content

    def all_url(self,all_url):
        start_html = self.request(all_url)
        all_a = bs(start_html.text,'lxml').find('div',class_='all').find_all('a')
        all_a.pop(0) #删除第一个无用的a标签 
        for img_url in all_a:
            title = img_url.get_text()
            path = str(title).replace("?",'_')  #取出系列的名字
            self.mkdir(path)  #循环生成文件夹
            href = img_url['href']  #每个系列的url
            self.html(href)
     
    def mkdir(self,path):
        path = path.strip() #
        is_exists = os.path.exists(os.path.join("E:\demo",path))
        if not is_exists:
            print('剪了个名字叫：',path,'的文件夹')
            os.makedirs(os.path.join("E:\demo",path))
            os.chdir(os.path.join("E:\demo",path))
        else:
            print('名字：',path,'的文件夹已存在')
            return False
                
    def html(self,href):
        html = self.request(href)
        self.headers['referer'] = href #得到每个系列的url后，循环获取page的url
        max_span = bs(html.text,"lxml").find('div',class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1,int(max_span)+1):
            page_url = href + '/' +str(page)
            self.img(page_url)

    def img(self,page_url):
        img_html = self.request(page_url)
        img_url = bs(img_html.text,'lxml').find('div',class_='main-image').find('img')['src']
        self.save(img_url) #拼接url，保存图片

    def save(self,img_url):
        name = img_url[-9:-4]
        img = self.request(img_url)
        with open(name + ".jpg",'ab') as f:  
            f.write(img.content)


meizi = Meizi()
meizi.all_url('https://www.mzitu.com/all')
