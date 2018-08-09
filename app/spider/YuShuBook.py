# coding:utf-8
from flask import jsonify

from app.libs.Http import HTTP
from flask import current_app

class YuShuBook:
    per_page = 10

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        '''
        :books: [dict]
        '''
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        '''
        根据isbn搜索书籍
        :param isbn: isbn
        '''
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        '''
        根据关键字搜索书籍
        :param keyword: 关键字
        :param page: 页码
        '''
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], (page-1)*current_app.config['PER_PAGE'])
        result = HTTP.get(url)
        self.__file_collection(result)

    def __fill_single(self, data=None):
        '''
        填充数据
        :param data: book、字典类型
        '''
        if data:
            self.total = 1
            self.books.append(data)

    def __file_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']

    @property
    def first(self):
        '''
        获取第一本书，如果不存在，返回None
        :return: book-dict
        '''
        return self.books[0] if self.total>=1 else None

if __name__ == '__main__':
    # result = YuShuBook.search_by_isbn('9787308164207')
    # result = YuShuBook.search_by_keyword('腾讯')
    # print(result)
    c = False
    if not c:
        print('c is false')
    a = ''
    if not a:
        print('a is false')
    b = None
    if not b:
        print('b is false')
    # 如果or的前面是false（False、None 或 ''），表达式为后面的值
    print(False or 'hello')  # hello
    print('' or 'hello')  # hello
    print(None or 'hello')  # hello

