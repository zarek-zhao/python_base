#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 2:54
# @Author  : JiuWei
# @File    : 不占内存的方式file.py
# @Software: win10  python3.8.2
import os
# f = open("test.txt", "a+", encoding="utf-8")
# for i in range(10):
#     f.write("\n赵瑞航 男 23")
#
# f.close()
# 不占内存修改文件
new_file = "test_new.txt"
old_file = "test.txt"
f = open("test.txt", "r", encoding="utf-8")
f_new = open("test_new.txt", 'a', encoding="utf-8")

old_str = '江小薇'
new_str = '江薇'
f.seek(0)
for line in f:
    if '江小薇' in line:
        line = line.replace(old_str, new_str)
    f_new.write(line)
f.close()
f_new.close()
os.remove(old_file)
os.renames(new_file, old_file)


