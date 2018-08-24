#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.8.16
# 出现MySQLdb导入错误的时候调用下面导入方式
import pymysql

# 使用install_as_MySQLdb函数将pymysql MySQLdb一起使用
pymysql.install_as_MySQLdb()

from redis import StrictRedis


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


class DevelopmentConfig(Config):
    """开发模式"""
    DEBUG = True

class ProductionConfig(Config):
    """生产者模式下配置"""
    DEBUG = False

#  定义配置字典
config = {
    "development":DevelopmentConfig,
    "production":ProductionConfig
}
