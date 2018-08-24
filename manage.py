#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16
import redis as redis
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
# 出现MySQLdb导入错误的时候调用下面导入方式
import pymysql
# 使用install_as_MySQLdb函数将pymysql MySQLdb一起使用
from redis import StrictRedis

pymysql.install_as_MySQLdb()
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

    # 设置加密字符串
    SECRET_KEY = "/W73UULUS4UFO5omviuVZz6+Bcjs5+2nRdvmyYNq1wEryZsMeluALSDGxGnuYoKX"
    # 调整session存储位置(存储到redis)
    # 指明sesion存储到那种类型的数据库
    SESSION_TYPE = "redis"
    # 上面的指明的数据库的实例对象
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_NUM)
    # session数据需要加密
    SESSION_USE_SIGNER = True
    # 不设置永久存储
    SESSION_PERMANENT = False
    # 默认存储的有效时长 （没有调整之前默认值是timedelta(days=31)）
    PERMANENT_SESSION_LIFETIME = 86400 * 2



# 1.创建flask对象
app = Flask(__name__)
# 2.把配置信息注册到app里
app.config.from_object(Config)
# 3.创建Mysql对象
db = SQLAlchemy(app)
# 4.创建redis对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 5.CSRF验证测试,后端保护验证机制
# 提取cookie中的csrf_token和ajax请求头里面csrf_token进行比较验证操作
CSRFProtect(app)
# 6.创建session拓展类的对象（将session的存储调整到redis中)
Session(app)

if __name__ == '__main__':
    app.run()


