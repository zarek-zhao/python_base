#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 12:01
# @Author  : JiuWei
# @File    : 随机数.py
# @Software: win10  python3.7.6

import random

n = random.randint(0, 10)
print("猜数字游戏开始：")
while True:
    user_guess = int(input("你想猜的数(输入-1退出)："))
    if user_guess == int(n):
    # print("恭喜你猜对了，答案是：%d" % user_guess)
        print("""
***************************
恭喜你猜对了，答案是：%d
*************************** 
        """ % user_guess)
        print("猜数字游戏开始：")
        user_guess = int(input("你想猜的数(输入-1退出)："))
    elif user_guess != int(n):
        if user_guess > int(n):
            print("你猜错了,答案比你猜的小")
        else:
            print("你猜错了，答案比你猜的大")

    elif user_guess == -1:
        print("退出猜数字游戏")
        break
