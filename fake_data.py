#!/usr/bin/env python
# -*-coding: utf-8 -*-
'''
@author: fanleehao
@contact: fanleehao@gmail.com
@file: fake_data.py
@time: 2018/10/5 16:33
@desc: 伪造数据，用于验证或测试某些功能
'''

import random
import datetime
from uuid import uuid4

from app.models import db, User, Tag, Post

# user = User(id=str(uuid4()), username='fan', password='fan')
# db.session.add(user)
# db.session.commit()

user = db.session.query(User).filter_by(username='fan').first()
tag_one = Tag(id=str(uuid4()), name='Python')
tag_two = Tag(id=str(uuid4()), name='Flask')
tag_three = Tag(id=str(uuid4()), name='SQLALchemy')
tag_four = Tag(id=str(uuid4()), name='JMilkFan')
tag_list = [tag_one, tag_two, tag_three, tag_four]

ss = "Example Text"

for i in range(100):
    # 胡乱生产100篇博文
    new_post = Post(id=str(uuid4()), title="Post" + str(i))
    new_post.user = user
    new_post.publish_date = datetime.datetime.now()
    new_post.text = ss
    new_post.tags = random.sample(tag_list, random.randint(1, 3))
    db.session.add(new_post)

db.session.commit()
