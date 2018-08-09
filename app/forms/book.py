import re

from wtforms import Form, StringField, IntegerField, FloatField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    # DataRequired要求参数不能为空格
    q = StringField(validators=[DataRequired(message='关键字不能为空格'), Length(min=1,max=30, message='关键字的长度应该在1-30')])
    page = IntegerField(validators=[NumberRange(min=1, max=20)], default=1)

class BookForm(Form):
    title = StringField(validators=[DataRequired(message='书名不能为空')])
    author = StringField(validators=[DataRequired(message='作者不能为空')])
    price = FloatField(validators=[DataRequired(message='价格不能为空')])
    isbn = StringField(validators=[DataRequired(message='isbn不能为空'), Length(11, 11, message='长度为11位')])
    summery = StringField(validators=[DataRequired(message='介绍不能为空')])

    def validate_isbn(self, field):
        return re.match('^\d{11}$', field.data)