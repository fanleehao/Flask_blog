#!/usr/bin/env python
# -*-coding: utf-8 -*-
'''
@author: fanleehao
@contact: fanleehao@gmail.com
@file: views.py
@time: 2018/10/1 17:50
@desc: 视图函数的入口
'''

from flask import render_template
from sqlalchemy import func  # 数据库操作中的一些库函数

from main import app
from models import db, User, Post, Comment, Tag, posts_tags


@app.route('/')
@app.route('/<int:page>')
def home(page=1):
    posts = Post.query.order_by(Post.publish_date.desc()).paginate(page, 10)
    recent, top_tags = slider_bar()
    return render_template('home.html', posts=posts, recent=recent, top_tags=top_tags)


@app.route('/post/<string:post_id>')
def post(post_id):
    post = db.session.query(Post).get_or_404(post_id)
    tags = post.tags
    comments = post.comments.order_by(Comment.date.desc()).all()
    recent, top_tags = slider_bar()
    return render_template('post.html', post=post, tags=tags, comments=comments, recent=recent, top_tags=top_tags)


@app.route('/tag/<string:tag_name>')
def tag(tag_name):
    tag = db.session.query(Tag).filter_by(name=tag_name).first_or_404()
    posts = tag.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = slider_bar()
    return render_template('tag.html', tag=tag, posts=posts, recent=recent, top_tags=top_tags)


@app.route('/user/<string:username>')
def user(username):
    user = db.session.query(User).filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = slider_bar()
    return render_template('user.html', user=user, posts=posts, recent=recent, top_tags=top_tags)


def slider_bar():
    """
    desc: 侧边栏显示最近的5篇博文、每篇文章最多的5个标签
    :return:
    """
    # 最近5篇博文
    recent = db.session.query(Post).order_by(Post.publish_date.desc()).limit(5).all()
    # 标签
    top_tags = db.session.query(
        Tag, func.count(posts_tags.c.post_id).label('total')
    ).join(
        posts_tags
    ).group_by(Tag).order_by('total DESC').limit(5).all()
    return recent, top_tags
