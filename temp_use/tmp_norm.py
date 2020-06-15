# -*- coding: utf-8 -*-
# @Time    : 2020/5/27
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : tmp_norm.py
# @Software: PyCharm
# @Function: 

import numpy as np

# a = np.array([3, 4])
# 
# print("keepdims = False")
# print(np.linalg.norm(a))
# print(np.linalg.norm(a, ord=1))
# print(np.linalg.norm(a, ord=2))
# print(np.linalg.norm(a, ord=np.inf))
# 
# print("\nkeepdims = True")
# print(np.linalg.norm(a, keepdims=True))
# print(np.linalg.norm(a, ord=1, keepdims=True))
# print(np.linalg.norm(a, ord=2, keepdims=True))
# print(np.linalg.norm(a, ord=np.inf, keepdims=True))
epsilon = 3
v = 0.8

# p = (np.e**epsilon-1) / (np.e**epsilon+1) * v / 2 + 0.5
# print(p)

p = np.e**epsilon / (np.e**epsilon+1)
print(p)


f_pos = 0
f_neg = 0.5
f = (f_pos - f_neg) / (f_pos+f_neg+2*p-2)
r = (1-f_pos-f_neg) / (2*p-1)
print(f,r)