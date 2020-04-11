#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 16:56
# @Author  : JiuWei
# @File    : exercise.py
# @Software: win10  python3.8.2
"""
针对列表names=[‘金角大王’, ‘黑姑娘’, ‘rain’, ‘eva’, ‘狗蛋’, ‘银角大王’, ‘eva’,’鸡头’]进入以下操作

通过names.index()的方法返回第2个eva的索引值

把以上的列表通过切片的形式实现反转

打印列表中所有下标为奇数的值

通过names.index()方法找到第2个eva值 ，并将其改成EVA
"""

names = ["金角大王", "黑姑娘", "rain", 'eva', '狗蛋', '银角大王', 'eva', '鸡头']
first_eva = names.index("eva")
print(first_eva)
second_eva = names[first_eva + 1:].index("eva") + first_eva + 1
print("the second eva :", second_eva)
# 通过names.index()方法找到第2个eva值 ，并将其改成EVA
names[second_eva] = "EVA"
# 把以上的列表通过切片的形式实现反转
print(names[:: -1])
# 打印列表中所有下标为奇数的值
for i in range(len(names)):
    if names.index(names[i]) % 2 == 0:
        print(names[i],end=",")
