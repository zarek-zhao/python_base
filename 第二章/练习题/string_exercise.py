#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 18:24
# @Author  : JiuWei
# @File    : string_exercise.py
# @Software: win10  python3.7.6


# 请用代码实现：利用下划线将列表的每一个元素拼接成字符串，li＝[‘alex’, ‘eric’, ‘rain’]
li = ['alex', 'eric', 'rain']
print('_'.join(li))

"""
查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素。

li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
"""
li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}


# 查找列表或元组中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素。
def find_c(list_me):
    str_list = []
    for i in list_me:
        i_no_space = i.strip()
        if i_no_space[0] == 'a' or i_no_space == 'A':
            if i_no_space[-1] == 'c':
                str_list.append(i_no_space)
    return str_list


list1 = find_c(li)
list2 = find_c(tu)
print('list1:' + str(list1))
print('list2:' + str(list2))

for i in dic:
    i_no_space = dic[i].strip()
    if 'a' in i_no_space[0] or 'A' in i_no_space[0]:
        if 'c' in dic[i][-1]:
            print('DIC:' + dic[i])

# 有如下变量，请实现要求的功能
#
tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])

# 讲述元组的特性
# 元组的元素不可被改变，但是如果元组有一个可以被改变的元素，那么该元素可以被改变，例如：list
# 请问tu变量中的第一个元素“alex”是否可被修改？
# 不可以
# 请问tu变量中的”k2”对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
# 引用类型，可以被修改
# 去字典类型的值的三种方法：
# 1. 通过键来取 tu[key]
# 2. 通过转换成字符串来取(这个太憨了)
# 3. 通过循环来取
tu[1][2]["k2"].append("Seven")
print(tu)
# 请问tu变量中的”k3”对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
# k3对应的值时是元组类型，不可被修改
# 6、转换
#
#
#
# 将字符串s = “alex”转换成列表
s = "alex"
print(list(s))
# 将字符串s = “alex”转换成元祖
print(tuple(s))
# 将列表li = [“alex”, “seven”]转换成元组
li = ['alex', 'seven']
print(tuple(li))
# 将元组tu = (‘Alex’, “seven”)转换成列表
print(list(li))
# 将列表li = [“alex”, “seven”]转换成字典且字典的key按照10开始向后递增
di = dict(zip([i for i in range(10, len(li) + 10)], li))
print(di)

x = [i for i in range(0, 20, 2)]
print(x)
"""
Python里面有个很棒的语法糖（syntactic sugar），它就是 list comprehension ，
有人把它翻译成“列表推导式”，也有人翻译成“列表解析式”。名字听上去很难理解，但是看它的语法就很清晰了。
虽然名字叫做 list comprehension，但是这个语法同样适用于dict、set等这一系列可迭代（iterable）数据结构。
"""
dict1 = {"name": "zhao", "age": "14"}
changed = {value: key for key, value in dict1.items()}
print(changed)

list1 = [1, 2, 3, 4, 5, 6, 7]
changed_list1 = [x for x in range(10, len(li)+11)]
print(changed_list1)


# 7、元素分类
#
# 有如下值集合[11,22,33,44,55,66,77,88,99,90]，将所有大于66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中。
#
# 即：{‘k1’:大于66的所有值, ‘k2’:小于66的所有值}。（编程题）
num_set = (11, 22, 33, 44, 55, 66, 77, 88, 99, 90)
num_dic={}
num_dic["k1"] = []
num_dic["k2"] = []

for i in num_set:
    if i >= 66:
        num_dic["k1"].append(i)
    else:
        num_dic["k2"].append(i)
print(num_dic)


# 8、在不改变列表数据结构的情况下找最大值li = [1,3,2,7,6,23,41,243,33,85,56]。（编程题）
li = [1, 3, 2, 7, 6, 23, 41, 243, 33, 85, 56]
max_num = li[0]
for i in range(li.__len__()):
    max_num = li[i] if max_num < li[i] else max_num
print(max_num)

# 10、利用for循环和range输出9 * 9乘法表 。（编程题）

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (i, j, i * j), end=",")
    print("")


