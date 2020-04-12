#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 13:22
# @Author  : JiuWei
# @File    : 小球落地.py
# @Software: win10  python3.7.6

# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
height = 100.0
count = 10.0
height_result = 0
height_bounce = height
for i in range(10):
    height_bounce = (1/2)*height_bounce
    height_result += height_bounce

print("height=%f, height_bounce=%f, height_result=%f " % (height, height_bounce, height_result))




