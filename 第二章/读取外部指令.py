#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 3:35
# @Author  : JiuWei
# @File    : 读取外部指令.py
# @Software: win10  python3.8.2


# str.replace(old, new[, max])
import sys
import os
# print(sys.argv)            # argv就是外部的参数
# 利用sys模块，传入命令窗口的参数
old_str = sys.argv[1]
new_str = sys.argv[2]
filename = sys.argv[3]
new_filename = "executive_prep_new.csv"
count = 0
# 打开文件，并执行替换，和写入操作。
file = open(filename, "r", encoding="utf-8")
file_new = open("executive_prep_new.csv", "a", encoding="utf-8")
for line in file:
    line_new = line.replace(old_str, new_str)
    if line != line_new:
        count += 1
    file_new.write(line_new)
file.close()
file_new.close()
# 调用os模块，覆盖旧文件。
os.replace(new_filename, filename)
# 打印替换了多少处的内容
print("你替换了%d处" % count)



