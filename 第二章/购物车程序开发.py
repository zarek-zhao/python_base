#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 20:11
# @Author  : JiuWei
# @File    : 购物车程序开发.py
# @Software: win10  python3.8.2
"""
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
......
]
实现功能要求：
1、启动程序后，让用户输入工资，然后进入循环，打印商品列表和编号

2、允许用户根据商品编号选择商品

3、用户选择商品后，检测余额是否够，够就直接扣款，并加入购物车， 不够就提醒余额不足

4、可随时退出，退出时，打印已购买商品和余额
"""

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
g = {"name": "电脑", "price": 1999}
# salary = float(input("请输入你的工资："))
for i in g:
    print(i, g[i])
for i in goods:
    print(i["name"], i["price"])
#
# a = (1, 2, 3, 4, [1, 1, 1])
# a[4][1] = 5
#
# print(a)
#
# me = "zhaoruihang"
# print(me.find("a"))
# print(me.index("a"))


