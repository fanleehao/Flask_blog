#!/usr/bin/env python
# -*-coding: utf-8 -*-
'''
@author: fanleehao
@contact: fanleehao@gmail.com
@file: config.py
@time: 2018/9/30 12:54
@desc: 系统环境配置，主要是控制系统的使用环境，如测试、开发、产品
'''


class Config(object):
    """配置类基类"""
    SECRET_KEY = 'FANLEEHAO'
    # reCAPTCHA秘钥
    RECAPTCHA_PUBLIC_KEY = "6Le_vXMUAAAAAA3mhMEkLxvKnHlg39bl_1ZKbNhq"
    RECAPTCHA_PRIVATE_KEY = "6Le_vXMUAAAAAAkpLdgj7NhPTMca3gPZtQxra-vP"

class ProdConfig(Config):
    """产品环境配置"""
    pass


class DevConfig(Config):
    """开发环境配置"""
    DEBUG = True
    # mysql连接
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123@127.0.0.1:3306/flask_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    """测试环境配置"""
    pass
