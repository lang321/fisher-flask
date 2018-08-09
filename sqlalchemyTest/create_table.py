# coding:utf-8
'''
@author: fight139
@file: create_table.py
@time: 2018/7/25 11:42
@desc: 
'''
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


# 一对多
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    email = Column(String(32), unique=True)
    ctime = Column(DateTime, default=datetime.datetime.now)   # 传递函数
    extra = Column(Text, nullable=True)

    # 联级删除
    groupId = Column(Integer, ForeignKey("usergroup.id", ondelete='CASCADE'))
    userGroup = relationship("UserGroup", backref="gusers")

    __table_args__ = {
        # 字符编码
        'mysql_charset': 'utf8'
        # 引擎
        # UniqueConstraint('id', 'name', name='uix_id_name'),
        # Index('ix_id_name', 'name', 'email'),
    }
class UserGroup(Base):
    __tablename__ = 'usergroup'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


# 多对多
class Grade(Base):
    __tablename__ = 'grade'
    id = Column(Integer, primary_key=True, autoincrement=True)
    score = Column(Integer, default=0)

    # 联级删除,一般不会直接删除关联表，而是将state设置为0
    student_id = Column(Integer, ForeignKey('student.id', ondelete='CASCADE'))
    course_id = Column(Integer, ForeignKey('course.id', ondelete='CASCADE'))


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    # age = Column(Integer)

    # 与生成表结构无关，仅用于查询方便
    courses = relationship('Course', secondary='grade', backref='students')


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(64), nullable=False)

def init_db():
    engine = create_engine(
        "mysql+cymysql://root:123@127.0.0.1:3306/sqlalchemy1?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    Base.metadata.create_all(engine)

def del_db():
    """
        根据类删除数据库表
        :return:
        """
    engine = create_engine(
        "mysql+cymysql://root:123@127.0.0.1:3306/sqlalchemy1?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.drop_all(engine)

def init_data1():
    engine = create_engine("mysql+cymysql://root:123@127.0.0.1:3306/sqlalchemy1?charset=utf8", max_overflow=0,
                           pool_size=5)
    Session = sessionmaker(bind=engine)

    session = Session()
    # 方式一
    # session.add_all([UserGroup(name='用户组1'), UserGroup(name='用户组2')])
    # session.add_all([Users(name='admin', email='666@qq.com', extra='简介', groupId=1),
    #                  Users(name='admin', email='888@qq.com', extra='简介2', groupId=2),])
    # 方式二
    g1 = UserGroup(name='用户组3')
    g1.gusers = [Users(name='admin', email='777@qq.com', extra='简介', groupId=1)]
    session.add(g1)
    g2 = UserGroup(name='用户组4')
    g2.gusers = [Users(name='admin', email='999@qq.com', extra='简介2', groupId=2)]
    session.add(g2)


    session.commit()
    session.close()

def init_data2():
    engine = create_engine("mysql+cymysql://root:123@127.0.0.1:3306/sqlalchemy1?charset=utf8", max_overflow=0,
                           pool_size=5)
    Session = sessionmaker(bind=engine)

    session = Session()
    # 方式一
    # session.add_all([Student(name='张三'), Student(name='李四'), ])
    # session.add_all([Course(course_name='java'), Course(course_name='python'), ])
    #
    # session.commit()  # 这里必须先提交
    #
    # session.add_all([Grade(student_id=1, course_id=1),
    #                  Grade(student_id=1, course_id=2),
    #                  Grade(student_id=2, course_id=1), ])

    # 方式二
    # 自动插入Grade数据，仅仅插入id
    stu1 = Student(name='张三')
    stu1.courses = [Course(course_name='java'), Course(course_name='python'), ]
    session.add(stu1)

    session.commit()
    session.close()

if __name__ == '__main__':
    # init_db()
    # del_db()
    # init_data1()
    init_data2()