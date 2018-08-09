# coding:utf-8
'''
@author: fight139
@file: DbHelper.py
@time: 2018/7/26 14:58
@desc: 
'''

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from sqlalchemyTest.create_table import Users, Student, ClassInfo, Grade

# 创建连接池，单例
engine = create_engine("mysql+cymysql://root:123@127.0.0.1:3306/sqlalchemy1?charset=utf8", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

# 每次执行数据库操作时，都需要创建一个session，从连接池取出
session = scoped_session(Session)

# ############# 执行ORM操作 #############
# obj1 = Users(name="alex1", email='666@qq.com', extra='介绍')
# session.add(obj1)


# 查询
g = session.query(Grade).filter_by(class_id=1, student_id=1).first()
s = session.query(Student).filter_by(id=1).first()
c = session.query(ClassInfo).filter_by(id=1).first()

# 提交事务
session.commit()
# 关闭session
session.close()