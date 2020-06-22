# -*- coding: utf-8 -*-
# @Time    : 2020/6/22
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 0060.py
# @Software: PyCharm
# @Function: 
"""
60. 第k个排列
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"
"""

def mysolution(n, k):
    arr = [i+1 for i in range(n)]
    # 计算n!
    order = 1
    for i in range(1, n+1):
        order = order * i
    # print("order = ", order)

    k = k - 1

    res = ""
    for i in range(n, 0, -1):
        # print("arr = ", arr, " , k = ", k)
        order = order // len(arr)

        # print("order = ", order)
        index = k // order
        # print("index = ", index)
        k = k - order * index
        pop_item = arr[index]
        arr.remove(pop_item)
        # print("pop_item = ", pop_item)
        res = res + str(pop_item)
    return res


if __name__ == '__main__':
    # n,k = 3,3
    # print(mysolution(n,k))
    n = 3
    for i in range(1, 7):
        res = mysolution(n, i)
        print(i, res)