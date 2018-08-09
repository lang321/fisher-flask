# coding:utf-8

from . import create_app
from app.models.book import Book
from app.models.gift import Gift
from app.models.user import User

app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81, threaded=True)

