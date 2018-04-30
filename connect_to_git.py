#! /usr/bin python3
# _*_ coding:utf-8 _*_
# Author: hujiaming
"""
这是一个用于测试使用Python连接Redis数据库的文件
"""
import git
repo = git.Repo(r'/var/git')  # 使用repo来管理本地库
print("本地git库是否为空：", repo.bare)
print("没有被add的文件:", repo.untracked_files)  # 查看没有被add的文件
print("当前分支：", repo.active_branch)
index = repo.index  # 使用index来管理stage