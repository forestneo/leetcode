# -*- coding: utf-8 -*-
# @Time    : 2020/5/27
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : tmp_norm.py
# @Software: PyCharm
# @Function: 

import numpy as np


c = 30
p = 120


# 批发价格
w = 40
# 回购价格
b = 0
# 零售商购买数量
q = 0
# 市场需求
d = 100

profit_s = 2000 + w*q - c * q - b * max(q-d, 0)
profit_r = 2000 + p * min(d, q) - w * q + b * max(q-d, 0)


w = 100
b = 100
d = 100
for q in range(10, 151, 5):
    profit_s = 2000 + w*q - c * q - b * max(q-d, 0)
    profit_r = 2000 + p * min(d, q) - w * q + b * max(q-d, 0)
    print(q, profit_r)

# for w in range(90):
#     for b in range(10):
#         for q in range(10, 150, 5):
#             for d in range(100):
#                 profit_s = 2000 + w*q - c * q - b * max(q-d, 0)
#                 profit_r = 2000 + p * min(d, q) - w * q + b * max(q-d, 0)
#                 print(w, b, q, d, profit_s, profit_r)
#                 result.append([w, b, q, d, profit_s, profit_r])

# f = open("1.txt", 'w')
# for line in result:
#     f.write(line)
# f.close()

# print(profit_s, profit_r)