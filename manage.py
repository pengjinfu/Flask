#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16
import redis as redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis

# 定义配置类，并从中加载配置
class Config(object):
    """工程配置信息"""
    # 开启debug模式
    DEBUG = True

    # 配置MySQL数据库
    # 设置数据库的连接
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    # 关闭数据库的跟踪
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis数据库
    # 配置redis的连接
    REDIS_HOST = "127.0.0.1"
    # 配置redis的端口
    REDIS_PORT = 6379
    # 配置redis的第2个空间存储
    REDIS_NUM = 2



# 创建flask对象
app = Flask(__name__)
# 把配置信息注册到app里
app.config.from_object(Config)
# 创建Mysql对象
db = SQLAlchemy(app)
# 创建redis对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

if __name__ == '__main__':
    app.run()



