# -*- coding: utf-8 -*-
# @Time    : 2020/6/20
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 005.py
# @Software: PyCharm
# @Function: 

"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."
"""

def replaceSpace(s: str) -> str:

    # str_lst = s.split()
    # print(str_lst)
    # print("%20".join(str_lst))
    # return "%20".join(s.split())
    str_new = s.replace(" ", "%20")
    return str_new


def replaceSpace_new(s):
    new = ''
    for char in s:
        new += '%20' if char == ' ' else char
    return new


if __name__ == '__main__':
    s = "We  are happy."
    # s = "We"
    ret = replaceSpace_new(s)
    print(ret)