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
    pass

class ProdConfig(Config):
    """产品环境配置"""
    pass

class DevConfig(Config):
    """开发环境配置"""
    pass

class TestConfig(Config):
    """测试环境配置"""
    pass