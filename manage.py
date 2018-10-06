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
from app import models
from flask_migrate import Migrate, MigrateCommand
from app import app

# 使用程序app实例来初始化manage对象
manager = Manager(app)

# 构造一个管理数据库迁移的对象migrate
migrate = Migrate(app, models.db)

# 通过Server构建一个命令行的对象，方便操作环境
manager.add_command("server", Server())
# 顺便创建一个DB的命令操作环境
manager.add_command('db', MigrateCommand)


# 当前环境的shell终端
@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    # 确保有导入 Flask app object，否则启动的 CLI 上下文中仍然没有 app 对象
    # 在这里返回的dict中的值，便可以在shell中调用
    return dict(app=app, db=models.db, User=models.User, Post=models.Post, Comment=models.Comment, Tag=models.Tag)

if __name__ == '__main__':
    manager.run()