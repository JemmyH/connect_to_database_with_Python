#! /usr/bin python3
# _*_ coding:utf-8 _*_
# Author: hujiaming
"""
这是一个用于测试使用Python连接Redis数据库的文件
"""
import redis
print(redis.__file__)
re = redis.Redis(host= "127.0.0.1",port= "6379",db= 0)
print("数据库个数：",re.dbsize())
print("查看连接状态：", re.ping())
for i in re.keys():
    re.delete(i)
# 增加字符串记录
re.set("time","2018-4-30")
print(re.get("time"))
# 添加一条数字记录 并自增1
re.set("num1",1)
re.incr("num1")
print(re.get("num1"))
# 添加一条列表记录
if re.llen("mylist") > 0:
    re.delete("mylist")
re.lpush("mylist", "love")
re.lpush("mylist", "I")
re.rpush("mylist", "Python")
print(re.lrange("mylist", 0, 2))
# 增加一条哈希表记录----哈希记录表，即键值对类型的数据
if re.hlen("myhash") > 0:
    re.delete("myhash")
re.hset("myhash", "name", "hujiaming")
re.hset("myhash", "age", 21)
re.hset("myhash", "email", "hujm20151021@gmail.com")
print(re.hgetall("myhash"))
print(re.keys())