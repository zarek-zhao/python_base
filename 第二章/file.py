#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 1:01
# @Author  : JiuWei
# @File    : file.py
# @Software: win10  python3.8.2
#
# file = open("./hello.txt", mode="a")
# file.write("\nhello python")
# file.close()
#
# file = open("hello.txt", mode="r")
# print(file.read())
# file.close()
file = open("hello.txt", mode="r")
for line in file:
    line1 = str(line.split())
    print()

file.close()

