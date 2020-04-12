#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 12:50
# @Author  : JiuWei
# @File    : 模拟登陆.py
# @Software: win10  python3.7.6
import 第二章.边读边写 as my_os
import  os
"""
练习题2 —— 模拟登陆：

用户输入帐号密码进行登陆

用户信息保存在文件内

用户密码输入错误三次后锁定用户，下次再登录，检测到是这个用户也登录不了

可优化点：
从文件中获取flag，并显示给用户
用户若是没有输入正确的账户，也要进行处理
结构过于混乱，可以更加清晰和简单，以后再来
等等
"""

user_info_file = "用户信息.txt"
user_info_file_new = "用户信息_new.txt"

# flag 用户登陆可尝试的次数，保存在文件中
# count 用户信息文件的行数, 修改信息时使用

count = 0
flag = 3
info_file = open(user_info_file, "r", encoding="utf-8")
info_file_new = open(user_info_file_new, "w", encoding="utf-8")
login_in = False
while True:
    user_name = input("请输入您的账号：")
    user_password = input("请输入您的密码：")
    info_file.seek(0)  # 每次查询完用户信息文件后，将光标置于文件的开头(也可以重新打开文件，不过不建议)，这一步卡了好久，以后要注意。
    for line1 in info_file:
        line = line1.split(",")
        # print(line, end="")
        if int(line[2]) >= 0 and flag == 3 and user_name == line[0]:
            flag = int(line[2])
            if flag == 0:
                break
        # print(line)
        # 判断用户信息中是否含有该用户且密码正确且用户是否被锁定
        # 如果判断正确，则登录成功，退出循环（执行其他模块）
        if user_name == line[0] and user_password == line[1] and flag > 0:
            print("登录成功")
            info_file.close()
            login_in = True
            break
        # 如果判断错误，先输出错误信息，再将flag减一，最后判断flag的次数是否为0
        # flag：是每一个用户登陆时可以尝试的次数，如果为0，则锁定账户
        if user_name == line[0]:
            break
        if flag == 3:  # 如果不是第一次查询用户信息文件，则不需要将行数增加(因为之前已经找出了用户所在的位置）
            count += 1
    # print(count)
    if login_in:
        my_os.rw(user_info_file, user_info_file_new, count, login_in)
        break
    if flag > 1:
        print("登陆失败，用户或密码错误,请重新输入，您还有%d次机会" % (flag-1))
    else:
        print("该用户已被锁定，请联系管理员解决")
    flag -= 1
    if flag <= 0:
        my_os.rw(user_info_file, user_info_file_new, count, login_in)
        break
info_file.close()
info_file_new.close()
os.remove(user_info_file)
os.rename(user_info_file_new, user_info_file)