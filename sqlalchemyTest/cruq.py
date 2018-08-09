# coding:utf-8
'''
@author: fight139
@file: cruq.py
@time: 2018/7/29 10:22
@desc: 
'''


from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from sqlalchemyTest.create_table import Users, Student, Course, Grade, UserGroup

# 创建连接池，单例
engine = create_engine("mysql+cymysql://root:123@127.0.0.1:3306/sqlalchemy1?charset=utf8", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

# 每次执行数据库操作时，都需要创建一个session，从连接池取出
# session = scoped_session(Session)
session = Session()


def add():
    obj1 = Users(name="alex2", email='888@qq.com', extra='介绍')
    session.add_all([obj1])
    # 提交事务
    session.commit()

def remove():
    # session.query(Users).filter(Users.id > 1).delete()
    # session.query(UserGroup).filter(UserGroup.id==1).delete()
    # session.query(Student).filter(Student.id==2).delete()
    session.query(Course).filter(Course.id==2).delete()
    # 提交事务
    session.commit()

def update():
    session.query(Users).filter(Users.id > 1).update({'name':'admin', 'extra':'hello'})
    session.query(Users).filter(Users.id > 0).update({Users.name:'admin-'+Users.name, 'extra':'hello'}, synchronize_session=False)
    session.query(Users).filter(Users.id > 0).update({Users.name:'admin-'+Users.name, 'extra':'hello'}, synchronize_session='evaluate')
    # 提交事务
    session.commit()

def select():
    # 查询
    # g = session.query(Grade).filter_by(class_id=1, student_id=1).first()
    # s = session.query(Student).filter_by(id=1).first()
    # c = session.query(ClassInfo).filter_by(id=1).first()

    users = session.query(Users).filter(Users.id>0).all()
    users2 = session.query(Users.name.label('n'), Users.email).all()
    userGroup = session.query(UserGroup).all()

    # left join
    res1 = session.query(Student, Grade).join(Grade, Grade.student_id==Student.id).all()
    res2 = session.query(Student.name, Grade.score).join(Grade, Grade.student_id==Student.id).all()

    ret3 = session.query(Grade).all()

    pass

# add()
# select()
remove()
# update()

# 关闭session
session.close()