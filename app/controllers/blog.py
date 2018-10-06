#!/usr/bin/env python
# -*-coding: utf-8 -*-
'''
@author: fanleehao
@contact: fanleehao@gmail.com
@file: blog.py
@time: 2018/10/1 17:50
@desc: blog博客展示页的单独模块蓝本
'''

from flask import render_template, Blueprint, redirect, url_for
from sqlalchemy import func  # 数据库操作中的一些库函数
import os

from app.models import db, User, Post, Comment, Tag, posts_tags
from app.forms import CommentForm, PostForm
from uuid import uuid4
import datetime


# 定义一个Blueprint类blog
blog_blueprint = Blueprint('blog', __name__, template_folder=os.path.join(os.path.pardir, 'templates', 'blog'), url_prefix='/blog')


@blog_blueprint.route('/')
@blog_blueprint.route('/<int:page>')
def home(page=1):
    posts = Post.query.order_by(Post.publish_date.desc()).paginate(page, 10)
    recent, top_tags = slider_bar()
    return render_template('home.html', posts=posts, recent=recent, top_tags=top_tags)


@blog_blueprint.route('/post/<string:post_id>', methods=('GET', 'POST'))
def post(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(id=str(uuid4()), name=form.text.data)
        new_comment.text = form.text.data
        new_comment.date = datetime.datetime.now()
        new_comment.post_id = post_id
        db.session.add(new_comment)
        db.session.commit()

    post = Post.query.get_or_404(post_id)
    tags = post.tags
    comments = post.comments.order_by(Comment.date.desc()).all()
    recent, top_tags = slider_bar()
    return render_template('post.html', post=post, tags=tags, comments=comments, form=form, recent=recent, top_tags=top_tags)


@blog_blueprint.route('/tag/<string:tag_name>')
def tag(tag_name):
    tag = Tag.query.filter_by(name=tag_name).first_or_404()
    posts = tag.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = slider_bar()
    return render_template('tag.html', tag=tag, posts=posts, recent=recent, top_tags=top_tags)


@blog_blueprint.route('/user/<string:username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = slider_bar()
    return render_template('user.html', user=user, posts=posts, recent=recent, top_tags=top_tags)


@blog_blueprint.route('/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        newpost = Post(str(uuid4()), title=form.title.data)
        newpost.text = form.text.data
        newpost.publish_date = datetime.datetime.now()

        db.session.add(newpost)
        db.session.commit()
        return redirect(url_for('blog.home'))

    return render_template('new_post.html', form=form)


@blog_blueprint.route('/edit/<string:id>', methods=['GET', 'POST'])
def edit_post(id):
    """View function for edit_post."""

    post = Post.query.get_or_404(id)
    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.text = form.text.data
        post.publish_date = datetime.datetime.now()

        # Update the post
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.post', post_id=post.id))

    form.title.data = post.title
    form.text.data = post.text
    return render_template('edit_post.html', form=form, post=post)


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
