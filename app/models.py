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
# from __init__ import app

# 数据库初始化迁移迁移到init中
db = SQLAlchemy()


class User(db.Model):
    # 用户表的对象模型，这个User类继承了db.Model后，SQLAlchemy与数据库的链接已经自动打通了
    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    # 定义被参照关系
    posts = db.relationship('Post', backref='users', lazy='dynamic')

    def __init__(self, id, username, password):
        # 省略的话 SQLAlchemy 会自动创建构造器, 并且所有定义的字段名将会成为此构造器的关键字参数名
        # 如 def __init__(self, id, username, password):
        # self.username = username

        # 修改
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        # 返回这个对象的字符串表示，而不是格式化的
        # 返回的是字符串表达式，可以使用eval处理
        # 与repr()类似, 将对象转化为便于供Python解释器读取的形式, 返回一个可以用来表示对象的可打印字符串.
        return "<Model User `{}`>".format(self.username)


# 关联关系的定义
posts_tags = db.Table('posts_tags',
                      db.Column('post_id', db.String(45), db.ForeignKey('posts.id')),
                      db.Column('tag_id', db.String(45), db.ForeignKey('tags.id')))


class Post(db.Model):
    # 发表的博文对象模型，与用户是多对一的关系
    __tablename__ = 'posts'
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)
    # 参考外键
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))  # 对应users表的id字段
    # 被参考关系
    comments = db.relationship('Comment', backref='posts', lazy='dynamic')
    # 关联的被参考关系：posts/tags多对多
    tags = db.relationship('Tag', secondary=posts_tags, backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __repr__(self):
        return "<Model Post `{}`>".format(self.title)


class Tag(db.Model):
    # 博文标签模型
    __tablename__ = 'tags'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Model Tag `{}`>".format(self.name)


class Comment(db.Model):
    # 博文评论模模型对象

    __tablename__ = 'comments'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    # 外键
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<Model Comment `{}`>'.format(self.name)
