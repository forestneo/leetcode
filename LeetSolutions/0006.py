# -*- coding: utf-8 -*-
# @Time    : 2020/3/20
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 0006.py
# @Software: PyCharm
# @Function: 

"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""

# LDREOEIIECIHNTSG
# LDREOEIIECIHNTS

def convert(s, numRows):
    if numRows == 1:
        return s
    ret = ['' for i in s]
    put_index = 0
    for i in range(numRows):
        pattern_1, pattern_2 = 2*(numRows-1) - 2*i,  2*i
        index = i
        if pattern_1 == 0 or pattern_2 == 0:
            # 第一种模式，只存在一次跳转
            pattern_1 = pattern_1 + pattern_2
            while index < len(s):
                ret[put_index] = s[index]
                put_index += 1
                index += pattern_1
        else:
            # 第二种模式，存在两次跳转
            while index < len(s):
                ret[put_index] = s[index]
                put_index += 1
                if not index + pattern_1 < len(s):
                    break
                index = index + pattern_1
                ret[put_index] = s[index]
                put_index = put_index + 1
                index = index + pattern_2
    return ''.join(ret)


if __name__ == '__main__':
    s = "AB"
    numRows = 1
    print(convert(s, numRows))