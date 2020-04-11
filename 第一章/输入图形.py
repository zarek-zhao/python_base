#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 13:01
# @Author  : JiuWei
# @File    : 输入图形.py
# @Software: win10  python3.8.2

i = 1

while i != 10:
    if i <= 5:
        j = 0
        while j != i:
            print("*", end="")
            j += 1
    else:
        j = 10 - i
        while j != 0:
            print("*", end="")
            j -= 1
    print("")
    i += 1



