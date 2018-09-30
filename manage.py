#!/usr/bin/env python
# -*-coding: utf-8 -*-
'''
@author: fanleehao
@contact: fanleehao@gmail.com
@file: manage.py
@time: 2018/9/30 14:47
@desc: manage和server是flask中的一些拓展，使用这些来进行命令行的管理与操作
        这些都是基于Flask-scripts拓展中的，一些工具，协助开发和debug
'''

from flask_script import Manager, Server
import main
import models

# 使用程序app实例来初始化manage对象
manage = Manager(main.app)

# 通过Server构建一个命令行的对象，方便操作环境
manage.add_command("server", Server())


@manage.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    # 确保有导入 Flask app object，否则启动的 CLI 上下文中仍然没有 app 对象
    # 在这里返回的dict中的值，便可以在shell中调用
    return dict(app=main.app, db=models.db, User=models.User)

if __name__ == '__main__':
    manage.run()