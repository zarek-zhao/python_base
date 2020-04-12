#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 12:55
# @Author  : JiuWei
# @File    : 循环加减和.py
# @Software: win10  python3.7.6

# 使用while循环实现输出2-3+4-5+6…+100 的和
number = 2
sum = 0
while number <= 100:
    if number % 2 == 0:
        sum = sum + number
    else:
        sum = sum - number
    number += 1
print("输出为：%d" % sum)
