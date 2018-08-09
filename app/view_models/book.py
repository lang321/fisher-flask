# coding:utf-8
'''
@author: fight139
@file: book.py
@time: 2018/7/19 14:50
@desc: 
'''


class BookViewModel(object):

    def __init__(self, data):
        '''
        :param data: dict
        '''
        self.title = data.get('title'),
        self.author = data.get('author'),
        self.price = str(data.get('price'))+'元',
        self.summery = data.get('summery')


class BookCollection(object):
    def __init__(self):
        self.books = []
        self.total = 0
        self.keyword = ''
    def fill(self, books, keyword):
        '''
        :param books: [BookViewModel]
        :param keyword:
        :return:
        '''
        self.total = len(books)
        self.books = [book for book in books]
        self.keyword = keyword





# @classmethod
#     def package_single(cls, data, keyword):
#         '''
#         :param data: book object
#         :param keyword:
#         :return:
#         '''
#         result = {
#             'books': [],
#             'total': 0,
#             'keyword': keyword
#         }
#         if data:
#             result['total'] = 1
#             # 对原始数据进行更改
#             result['books'] = [cls.__cut_book_data(data)]
#         return result
#
#     @classmethod
#     def package_collection(cls, data, keyword):
#         result = {
#             'books': [],
#             'total': 0,
#             'keyword': keyword
#         }
#         if data:
#             result['total'] = len(data)
#             for b in data:
#                 # 对原始数据进行更改
#                 result['books'].append(cls.__cut_book_data(b))
#
#         return result
#
#     @classmethod
#     def __cut_book_data(cls, data):
#         result = {
#             'title': data['title'],
#             'author': data['author'],
#             'price': data['price'],
#             'summery': data['summery']
#         }
#         return result