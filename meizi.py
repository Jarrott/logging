import requests as r
from bs4 import BeautifulSoup as Bea
import os

class meizi():
    def __init__(self):
        #浏览器请求头
        self.headers = {'User-Agent':"Mozilla/5.0(Windows NT 6.1;WOW64) AppleWebKit/5377.1 (KHTML,like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    
    def all_url(self,all_url):
        start_html = self.request(all_url) #携带header头请求所有图片的地址
        #使用beautifulsoup解析获取的html代码，解析器为lxml （parser行不）
        all_a = Bea(start_html.text,"lxml").find('div',class_='all').find_all('a') #find选中class = all的div，找出所有的a标签
        all_a.pop(0)  #为什么要删除第一个a标签？
        for a in all_a:    #遍历所有的a标签
            title = a.get_text()  #获取a标签的title
            path = str(title).replace("?",'_')
            self.mkdir(path)
            href = a['href']       #每个系列的url
            self.html(href)

    def html(self,href):
        html = self.request(href)  #循环请求每个a标签的href
        self.headers['referer'] = href
        #不删除第一个a标签的时候报错find_allno attribute 'find_all'find_all('span')[-2].get_text()从倒数第二个span开始往上获取？
        max_span = Bea(html.text,'lxml').find('div',class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1,int(max_span)+1):  
            page_url = href + '/' + str(page)
            self.img(page_url)

    def img(self,page_url):
        img_html = self.request(page_url)
        img_url = Bea(img_html.text,'lxml').find('div',class_='main-image').find('img')['src']
        self.save(img_url)


    def save(self,img_url):        
        name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name+'.jpg','ab')  #写入多媒体文件必须要 b 这个参数
        f.write(img.content)        #多媒体文件要有content
        f.close()


    def mkdir(self,path):
        path = path.strip()
        isExists = os.path.exists(os.path.join("E:\demo",path))
        if not isExists:
            print(u'捡了一个名字叫',path,u'的文件夹')
            os.makedirs(os.path.join("E:\demo",path))
            return True
        else:
            print(u'名字叫',path,u'的文件夹已经存在了')
            return False


    def request(self,url):
        content = r.get(url,headers = self.headers)
        return content
    
Meizi = meizi()
Meizi.all_url('http://www.mzitu.com/all')