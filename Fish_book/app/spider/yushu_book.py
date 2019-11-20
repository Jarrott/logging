import requests
from app.libs.httper import Http
from flask import current_app

"""http://t.yushu.im
    关键字搜索：
    http://t.yushu.im/v2/book/search?q={}&start={}&count={}
    isbn搜索：
    http://t.yushu.im/v2/book/isbn/{isbn}
    豆瓣api:
    https://api.douban.com/v2/book
"""


class YuShuBook:
    isb_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = '    http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isb_url.format(isbn)
        result = Http.get(url)
        self.__fill_single(result)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def search_by_keyword(self, keyword, page):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = Http.get(url)
        self.__fill_collection(result)
        return result

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None
