# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/03/12 <https://www.soo9s.com>
"""
import requests as r
import os
import lxml

from bs4 import BeautifulSoup as bs


class MeiZi:
    def __init__(self):
        # 浏览器请求头
        self.headers = {
            'User-Agent': "Mozilla/5.0(Windows NT 6.1;WOW64) AppleWebKit/5377.1 \
            (KHTML,like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

    def all_url(self, all_url):
        start_html = self.request(all_url)  # 携带header头请求所有图片的地址
        # 使用beautifulsoup解析获取的html代码，解析器为lxml （parser行不）
        all_a = bs(start_html.text, "lxml").find('div', class_='all').find_all('a')  # find选中class = all的div，找出所有的a标签
        all_a.pop(0)  # 为什么要删除第一个a标签？
        for img_url in all_a:  # 遍历所有的a标签
            title = img_url.get_text()  # 获取a标签的title
            path = str(title).replace("?", '_')
            self.mkdir(path)
            href = img_url['href']  # 每个系列的url
            self.html(href)

    def html(self, href):
        html = self.request(href)  # 循环请求每个a标签的href
        self.headers['referer'] = href
        # 不删除第一个a标签的时候报错find_allno attribute 'find_all'find_all('span')[-2].get_text()从倒数第二个span开始往上获取？
        max_span = bs(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url)

    def img(self, page_url):
        img_html = self.request(page_url)
        img_url = bs(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)

    def save(self, img_url):
        name = img_url[-9:-4]
        img = self.request(img_url)
        with open(name + ".jpg", 'ab') as f:
            f.write(img.content)

    def mkdir(self, path):
        path = path.strip()
        # / Users / xujiaqi /.code / pro / py - gui / share / zyb_share / app / zyb_wx_bot / demo
        is_exists = os.path.exists(os.path.join("./demo", path))
        if not is_exists:
            print('捡了一个名字叫', path, '的文件夹')
            os.makedirs(os.path.join("./demo", path))
            return True
        else:
            print('名字叫', path, '的文件夹已经存在了')
            return False

    def request(self, url):
        content = r.get(url, headers=self.headers)
        return content


meizi = MeiZi()
meizi.all_url('http://www.mzitu.com/all')
