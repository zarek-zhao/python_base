#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 12:29
# @Author  : JiuWei
# @File    : 判断登录.py
# @Software: win10  python3.7.6
# 实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次

user_name = input("请输入用户名：")
user_password = input("请输入密码：")
count = 3
while count != 0:
    if user_name == "seven" or user_name == "alex" and user_password == "123":
        print("欢迎您，用户%s,您已登陆成功" % user_name)
        break
    else:
        print("登陆失败，用户名或密码错误，您可以再尝试%d次" % count)
        user_name = input("请输入用户名：")
        user_password = input("请输入密码：")
        count -= 1






