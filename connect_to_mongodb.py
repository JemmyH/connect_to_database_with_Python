#! /usr/bin python3
# _*_ coding:utf-8 _*_
# Author: hujiaming
"""
这是一个用于测试使用Python连接MongoDB数据库的文件
"""
import pymongo
user_id = 'hujiaming'
password = '123456'
database = 'hujiaming'
mongodb_uri = "mongodb://" + user_id + ":" + password + "@127.0.0.1:27017"
print(mongodb_uri)  # 打印出MongoDB的连接信息
client = pymongo.MongoClient(mongodb_uri)
db = client.hujiaming
collection = db.students
student1 = {
    'id': '1512054',
    'name': 'hujiaming',
    'age': 20,
    'gender': 'male'
}
result = collection.insert_one(student1)  # 插入一条数据
print([i for i in collection.find()])  # 输出名叫hujiaming的数据库的名叫students的collection的所有数据
print(collection.find_one())  # 返回集合中单条数据
collection.update({'name': 'hujiaming'}, {'id': '1512054', 'name': 'changed_name', 'age': 20, 'gender': 'male'})  #更新数据
print([i for i in collection.find()])  # 打印更新后的数据
collection.remove()  # 删除这个collection中的所有数据
collection.drop()  # 删除这个collection