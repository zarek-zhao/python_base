#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 15:38
# @Author  : JiuWei
# @File    : 1.py
# @Software: win10  python3.7.6
user_info_file = "用户信息.txt"
user_info_file_new = "用户信息.txt"
info_file = open(user_info_file, "r", encoding="utf-8")
info_file_new = open(user_info_file_new, "w", encoding="utf-8")
count = 0
user_name = input("请输入您的账号：")
user_password = input("请输入您的密码：")
while True:
    info_file.seek(0)
    for line1 in info_file:
        line = line1.split(",")
        if user_name == line[0]:
            break
        count += 1
    print(count)

#