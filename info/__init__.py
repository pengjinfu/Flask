#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect


from config import *
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