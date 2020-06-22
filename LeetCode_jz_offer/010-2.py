# -*- coding: utf-8 -*-
# @Time    : 2020/6/22
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 010-2.py
# @Software: PyCharm
# @Function: 
"""
剑指 Offer 10- II. 青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
提示：
0 <= n <= 100
"""

class Solution:
    def numWays(self, n: int) -> int:
        a, b = 0, 1
        mod = 10**9 + 7
        for i in range(n):
            a, b = b, (a+b) % mod
        return b

if __name__ == '__main__':
    pass