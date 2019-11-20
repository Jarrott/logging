class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.price = book['price']
        self.pages = book['pages']
        self.summary = book['summary']
        self.image = book['image']
        self.isbn = book['isbn']
        self.pubdate = book['pubdate']
        self.binding = book['binding']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return '/'.join(intros)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class Book_ViewModel:
    # 单条数据的处理返回
    @classmethod
    def package_single(cls, data, keyword):
        result = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            result['total'] = 1
            result['books'] = [cls.__cut_book_data(data)]
        return result

    # 多条数据的处理返回
    @classmethod
    def package_collection(cls, data, keyword):
        result = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            result['total'] = data['total']
            result['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return result

    # 筛选有用数据
    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'price': data['price'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']) or '',
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book


"""定义类的核心：
    #使用类变量，实力变量描述特征
    #使用类方法规范行为
"""
