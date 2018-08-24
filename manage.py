#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import app, db

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@app.run('/')
def index():
    return "index"


if __name__ == '__main__':
    app.run()
