# -*- coding: utf-8 -*-
# @Time    : 2020/6/21
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 0069.py
# @Software: PyCharm
# @Function: 

"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
由于返回类型是整数，小数部分将被舍去。
"""

def mysqrt(x):
    # 二分法
    left = 0
    right = x + 1

    while right - left > 1:
        middle = (left + right) // 2
        if middle ** 2 > x:
            right = middle
        else:
            left = middle
        print(left, right)
    return left


if __name__ == '__main__':
    x = 8
    res = mysqrt(x)
    pass