#!/usr/bin/env python
# -*-coding: utf-8 -*-
'''
@author: fanleehao
@contact: fanleehao@gmail.com
@file: forms.py
@time: 2018/10/5 17:53
@desc: 表单
'''

from flask_wtf import Form
from wtforms import StringField, TextField
from wtforms.validators import DataRequired, Length


class CommentForm(Form):
    """评论表单验证"""
    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    text = TextField(u'Comment', validators=[DataRequired()])
