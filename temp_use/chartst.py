# -*- coding: utf-8 -*-
# @Time    : 2020/6/17
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : chartst.py
# @Software: PyCharm
# @Function: 

# row, col = 3, 5
# visited = [[0] * col] * row
# print(visited)
# visited[1][1] = 1
# print(visited)

import numpy as np

a = np.zeros(shape=(3,2), dtype=bool)
b = a.copy()
a[0][0] = 1
print(a)
print(b)
b = a.copy()
print(b)

