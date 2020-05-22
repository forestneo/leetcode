# -*- coding: utf-8 -*-
# @Time    : 2020/3/30
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : my01.py
# @Software: PyCharm
# @Function: 
import sys


def find_max_index(lst: list):
    max_index = 0
    for i in range(len(lst)):
        if lst[i] > lst[max_index]:
            max_index = i
    return max_index


n, m, k = 3, 3, 100
a = [100, 200, 400]
n, m, k = map(int,sys.stdin.readline().strip().split())
line = sys.stdin.readline().strip()
a = list(map(int, line.split()))


for day in range(m):
    # 鸡繁殖
    for i in range(len(a)):
        a[i] = a[i] + k
    # 最大的变成一半
    max_index = find_max_index(a)
    a[max_index] = int(a[max_index] / 2)
print(sum(a))
