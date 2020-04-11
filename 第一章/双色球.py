#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 12:27
# @Author  : JiuWei
# @File    : 双色球.py
# @Software: win10  python3.8.2
"""
双色球彩票 选购程序

先让用户依次选择6个红球，再选择2个蓝球，最后统一打印用户选择的球号。

确保用户不能选择重复的，选择的数不能超出范围。
"""
ball_list = []
red_ball_list = []
blue_ball_list = []
i = 0
j = 0
# 选取红色球，只能选取0-32的球
while i != 6:
    try:
        red_ball = int(input("\033[1;31mplease select your red ball:\033[0m"))
        if 0 < int(red_ball) < 32:
            if int(red_ball) in red_ball_list:
                print("\33[1;37myou can't choose repeat ball\33[0m")
            else:
                red_ball_list.append(red_ball)
                i += 1
        else:
            print("\33[1;37ymou only can select ball between 0-32\33[0m")
    except ValueError:
        print("\33[1;37myou only can select ball between 0-32\33[0m")
# 选取蓝色球，只能选取0-32的球
while j != 2:
    try:
        blue_ball = int(input("\033[1;34mplease select your blue ball:\033[0m"))
        if 0 < int(blue_ball) < 32:
            if int(blue_ball) in blue_ball_list:
                print("\33[1;37myou can't choose repeat ball\33[0m")
            else:
                blue_ball_list.append(blue_ball)
                j += 1
        else:
            print("\33[1;37myou only can select ball between 0-32\33[0m")
    except ValueError:
        print("\33[1;37myou only can select ball between 0-32\33[0m")

print("\33[1;33myour ball list is :\33[0m")

# 输出所选择的双色球号
print("Red Ball  :"+str(red_ball_list))
print("Blue Ball :"+str(blue_ball_list))
print("Good Luck")
