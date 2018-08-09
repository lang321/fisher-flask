# coding:utf-8
import json

from flask import jsonify, request, Request, session, render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash

from app import db
from app.forms.auth import RegisterForm
from app.forms.book import SearchForm, BookForm
from app.models.book import Book
from app.models.gift import Gift
from app.models.user import User
from app.view_models.book import BookCollection, BookViewModel
from . import web


# 参数
@web.route('/book/search', methods=['POST'])
def search():
    q = request.args['q']
    # page = request.args.get('page')
    # print(q, page)
    # result = YuShuBook.search_by_keyword(q)


    # get 方式args
    form = SearchForm(request.args)
    if form.validate():
        print('验证通过')
        q = form.q.data.strip()  #去空格
        page = form.page.data
        # 调用业务逻辑层
        result = {'q': q, 'page': page}
        books = BookCollection()
        books.fill(books=[BookViewModel({'title': '三国演义', 'author': '吴承恩'}),
                          BookViewModel({'title': '水浒传', 'author': '施耐庵'})], keyword='四大名著')
        # return jsonify(books)
        return json.dumps(books, default=lambda o: o.__dict__)
    else:
        print('验证失败')
        return jsonify(form.errors)
@web.route('/')
@web.route('/index', methods=['GET'])
def index():
    data = {
        'name':'张三',
        'age':20
    }
    flash('登录成功', category='ok')
    flash('成功进入系统', category='error')
    return render_template('index.html', data=data)


@web.route('/hello2', endpoint='h1', redirect_to='/index')
def test1():
    user1 = User.query.filter_by(id=1).first()
    user2 = User.query.filter_by(id=2).first()
    gift = Gift.query.filter_by(id=1).first()
    return 'ok'

@web.route('/book/add', methods=['GET', 'POST'])
def add_book():
    form = BookForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit(throw=False):
            book = Book()
            book.set_attrs(form.data)
            db.session.add(book)
    return render_template('book/add_book.html', form=form)