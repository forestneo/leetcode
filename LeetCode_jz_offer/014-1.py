# -*- coding: utf-8 -*-
# @Time    : 2020/6/28
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 014-1.py
# @Software: PyCharm
# @Function: 

"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

提示：
2 <= n <= 58

"""

class Solution:
    def cuttingRope(self, n: int) -> int:
        rope = [0, 1, 1, 2, 4, 6, 9]
        if n <= 6:
            return rope[n]
        return 3 * self.cuttingRope(n-3)

if __name__ == '__main__':
    pass