#!/usr/bin/env python
# -*-coding: utf-8 -*-
'''
@author: fanleehao
@contact: fanleehao@gmail.com
@file: models.py
@time: 2018/9/30 15:53
@desc: 数据ORM模型类
'''

from flask_sqlalchemy import SQLAlchemy
from main import app

db = SQLAlchemy(app)

class User(db.Model):
    # 用户表的对象模型，这个User类继承了db.Model后，SQLAlchemy与数据库的链接已经自动打通了
    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username):
        # 省略的话 SQLAlchemy 会自动创建构造器, 并且所有定义的字段名将会成为此构造器的关键字参数名
        # 如 def __init__(self, id, username, password):

        
        self.username = username
    def __repr__(self):
        # 返回这个对象的字符串表示，而不是格式化的
        # 返回的是字符串表达式，可以使用eval处理
        # 与repr()类似, 将对象转化为便于供Python解释器读取的形式, 返回一个可以用来表示对象的可打印字符串.
        return "<Model User `{}`>".format(self.username)
