#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 20:15
# @Author  : JiuWei
# @File    : a.py
# @Software: win10  python3.7.6
# 11、求100以内的素数和。（编程题）
# for i in range(3, 101):
#     flag = False
#     for j in range(2, i):
#         if i%j == 0:
#             flag = True
#             break
#     if flag:
#         continue
#     else:
#         print(i,end=",")
# --------------------------------------------------------------------------------------
# prime_num = ["%s" % i for i in range(3, 101) if not [j for j in range(2, i) if i%j==0 ]]
# print("".join(prime_num))

# 筛选法求素数
prime_list = [i for i in range(100)]
prime_list[0], prime_list[1] = False, False
prime_list[2] = True
count = 2
for i in range(3, prime_list.__len__()):
    i = int(i)
    if i == True:
        if 2*i < 100:
            for i in range(i+i, 100, i):
                print(i, end=",")
                i = False
                count += 1
        else:
            break
    else:
        break

    print()
print(count)













