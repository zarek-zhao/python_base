#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 11:45
# @Author  : JiuWei
# @File    : if_else.py
# @Software: win10  python3.8.2

# 从用户哪里得到输入;

while(True):
    score = input("请输入你的成绩(输入0退出)：")
    if int(score) == 0:
        break
    if 0 < int(score) < 60:
        print("你的成绩不合格")
    elif int(score) < 80:
        print("你的成绩良好")
    elif int(score) < 100:
        print("你的成绩优秀")
    else:
        print("输入成绩失败,成绩超过判定的有效范围（0~100）")

