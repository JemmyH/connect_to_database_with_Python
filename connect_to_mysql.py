#! /usr/bin python3
# _*_ coding:utf-8 _*_
# Author: hujiaming
"""
这是一个用于测试使用Python连接MySQL数据库的文件
"""
import pymysql
conn = pymysql.Connect(host="127.0.0.1", port=3306, user="hujiaming", passwd="123456",db="hujiaming")
cursor = conn.cursor()
# cursor有三个属性：
# cursor.fetchone() “将结果集中的第一条取出“
# cuosor.fetchall() ”将所有的结果取出，如果事先执行了cursor,fetchone()，则此结果少一条”
# cuesor.rowcount() “返回受影响的结果条数”


def excute(sql, word):
    cursor.execute(sql)
    conn.commit()
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.rowcount,"option: ", word, "successfully")
    if word == "select":
        result = cursor.fetchall()
        for i in result:
            print(i)


if __name__ == '__main__':
    while True:
        try:
            sql = input("请输入需要执行的sql语句：").lower()
            word = sql.split()[0]
            if sql == "break":
                break
            else:
                excute(sql, word)
        except Exception as e:
            print("An error occured:", e)
        finally:
            if sql == "break":
                print("goodbye")
            else:
                print("input 'break' to quit.")