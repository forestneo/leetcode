# -*- coding: utf-8 -*-
# @Time    : 2020/6/23
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 0067.py
# @Software: PyCharm
# @Function: 
"""
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        a.reverse()
        b.reverse()
        if len(a) < len(b):
            a, b = b, a
        res = []
        flag = 0
        for i in range(len(a)):
            a_item = int(a[i])
            b_item = int(b[i]) if i in range(len(b)) else 0
            tmp_res = (a_item + b_item + flag) % 2
            flag = (a_item + b_item + flag) // 2
            res.append(str(tmp_res))
        if flag == 1:
            res.append(str(flag))
        res.reverse()
        res = ''.join(res)
        return res


if __name__ == '__main__':


    a = '1010'
    b = '1011'
    print(a)

    Sol = Solution()
    res = Sol.addBinary(a, b)
    print(res)
    pass