# -*- coding: utf-8 -*-
# @Time    : 2020/3/21
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 0009.py
# @Software: PyCharm
# @Function: 

"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:

你能不将整数转为字符串来解决这个问题吗？
"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    str_x = str(x)
    reverse_x = str_x[::-1]
    print(str_x)
    print(reverse_x)
    print(str_x == reverse_x)
    if str_x == reverse_x:
        return True
    return False


if __name__ == '__main__':
    x = 141
    print(isPalindrome(x))



















