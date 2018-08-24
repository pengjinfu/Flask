#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db


# 单一职责的原则：manage.py 仅仅作为项目启动文件即可
# 工厂方法的调用（ofo公司）
app = create_app("development")

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@app.run('/')
def index():
    return "index"


if __name__ == '__main__':
    app.run()
