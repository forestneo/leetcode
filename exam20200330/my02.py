# -*- coding: utf-8 -*-
# @Time    : 2020/3/30
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : my02.py
# @Software: PyCharm
# @Function: 

import sys


def my_solution(n, a):
    my_sum = 0
    cnt = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            my_sum += max(a[i:j])
            cnt += 1
    print("%.6f" % float(my_sum / cnt))


# n = 1
# a = [1]
n = int(sys.stdin.readline().strip().split()[0])
line = sys.stdin.readline().strip()
a = list(map(int, line.split()))


my_solution(n, a)