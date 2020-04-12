#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 13:40
# @Author  : JiuWei
# @File    : 边读边写.py
# @Software: win10  python3.7.6
"""

"""
import os


def rw(file1, file2, count_out, login_in):
    info_file = open(file1, "r", encoding="utf-8")
    info_file_new = open(file2, "w", encoding="utf-8")
    count_in = 0
    info_file.seek(0)
    info_file_new.seek(0)
    for line1 in info_file:
        line1 = line1.split(",")
        # print(line1, end="")
        # count = int(line1[2])
        # print(count)
        if login_in == False:
            if count_in == count_out:
                line1[2] = '0\n'
                line1 = ','.join(line1)
                info_file_new.write(line1)
                count_in += 1
                continue
        line1 = ','.join(line1)
        info_file_new.write(line1)
        count_in += 1
    info_file.close()
    info_file_new.close()

    # os.remove(file1)
    # os.renames(file2, file1)
    print("执行完成")

# user_info_file = "用户信息.txt"
# user_info_file_new = "用户信息.txt"
#
# info_file = open(user_info_file, "r", encoding="utf-8")
# info_file_new = open(user_info_file_new, "w", encoding="utf-8")
# count = 1
# file1 = open("1", "r")
# file2 = open("2", "w")
# rw(info_file, info_file_new, count)
