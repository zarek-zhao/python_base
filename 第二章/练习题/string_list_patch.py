#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 19:16
# @Author  : JiuWei
# @File    : string_list_patch.py
# @Software: win10  python3.7.6
# 写代码，有如下列表，按照要求实现每一个功能
li = ['alex', 'eric', 'rain']
#
# 计算列表长度并输出
print(li.__len__())
print(li)
# 列表中追加元素“seven”，并输出添加后的列表
li.append('seven')
print(li)
# 请在列表的第1个位置插入元素“Tony”，并输出添加后的列表
li.insert(0, 'Tony')
print(li)
# 请修改列表第2个位置的元素为“Kelly”，并输出修改后的列表
li.insert(1, 'Kelly')
print(li)
# 请删除列表中的元素“eric”，并输出修改后的列表
li.remove('eric')
print(li)
# 请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
print(li.pop(1))
print(li)
# 请删除列表中的第3个元素，并输出删除元素后的列表
print(li.pop(2))
print(li)
# 请删除列表中的第2至4个元素，并输出删除元素后的列表

# 请将列表所有的元素反转，并输出反转后的列表
li.reverse()
print(li)
# 请使用for、len、range输出列表的索引
for i in range(len(li)):
    print(i, end=",")
# 请使用enumrate输出列表元素和序号（序号从100开始）
print("\nenumerate:")
list = enumerate(li,start=0)
for index,value in list:
    print(index, value)


# 请使用for循环输出列表的所有元素
# for i in li:
#     print("\n"+i, end="")
#

# 写代码，有如下列表，请按照功能要求实现每一个功能

li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]

# 请根据索引输出“Kelly”
print(li[2][1][1])
# 请使用索引找到’all’元素并将其修改为“ALL”，如：li[0][1][9]…
li[2][2] = "ALL"
print(li[2][2])









