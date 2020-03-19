# -*- coding: utf-8 -*-
# @Time    : 2020/3/20
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 007.py
# @Software: PyCharm
# @Function: 

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""

def reverse_accept(x):
    flag = 1
    if x < 0:
        flag, x = -1, -x
    value = 0
    while x:
        value = value * 10 + x % 10
        x = int(x / 10)
    ret = flag * value
    if ret < -2 ** 31 or ret > 2 ** 31 - 1:
        return 0
    return ret


def reverse_with_str(x):
    str_value = str(x)
    reverse_value = str_value[::-1] if str_value[0] != '-' else '-'+str_value[1:][::-1]
    ret = int(reverse_value)
    if ret < -2 ** 31 or ret > 2 ** 31 - 1:
        return 0
    return ret

def reverse(x):
    pass


if __name__ == '__main__':
    print(reverse(123))
    print(reverse(0))
    print(reverse(-123))
    print(reverse(120))
    print(reverse(1534236469))