#!/usr/bin/env python
# -*-coding: utf-8 -*-
'''
@author: fanleehao
@contact: fanleehao@gmail.com
@file: main.py
@time: 2018/9/30 13:01
@desc: 主入口文件
'''

from flask import Flask, redirect, url_for
from config import DevConfig
from models import db
from controllers import blog, main
from extensions import bcrypt

# app = Flask(__name__)

# 从配置类中获取配置文件，使用from_object()
# 不使用 app.config['DEBUG'] 是因为这样可以加载 class DevConfig 的配置变量集合，而不需要一项一项的添加和修改。
# app.config.from_object(DevConfig)
# db.init_app(app)
# 导入视图函数——有蓝本后不再需要
# views = __import__('views')


# 加了蓝本后，必须要有一个入口app
# @app.route('/')
# def index():
#     return redirect(url_for('blog.home'))


# 根据不同状况动态创建APP对象
def create_app(object_name):
    """
    工厂模式的创建
    :param object_name: 不同的对象模式
    :return: 特定的app对象实例
    """
    app = Flask(__name__)
    app.config.from_object(object_name)
    # 数据库
    db.init_app(app)
    # Bcrypt加密库
    bcrypt.init_app(app)

    # 注册蓝本
    app.register_blueprint(blog.blog_blueprint)
    app.register_blueprint(main.main_blueprint)
    return app

if __name__ == '__main__':
    app = create_app()
    # 启动程序
    app.run()
