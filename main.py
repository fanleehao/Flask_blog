#!/usr/bin/env python
# -*-coding: utf-8 -*-
'''
@author: fanleehao
@contact: fanleehao@gmail.com
@file: main.py
@time: 2018/9/30 13:01
@desc: 主入口文件
'''

from flask import Flask
from config import DevConfig

app = Flask(__name__)

# 从配置类中获取配置文件，使用from_object()
# 不使用 app.config['DEBUG'] 是因为这样可以加载 class DevConfig 的配置变量集合，而不需要一项一项的添加和修改。
app.config.from_object(DevConfig)

# 路由规则
@app.route('/')
def home():
    return '<h1>Hello,world<h1>'

if __name__ == '__main__':
    # 启动程序
    app.run()