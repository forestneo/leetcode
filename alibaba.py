# -*- coding: utf-8 -*-
# @Time    : 2020/3/26
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : alibaba.py
# @Software: PyCharm
# @Function: 


"""
给出一个正整数N和长度L，找出一段长度大于等于L的连续非负整数，他们的和恰好为N。答案可能有多个，我我们需要找出长度最小的那个。
例如 N = 18 L = 2：
5 + 6 + 7 = 18
3 + 4 + 5 + 6 = 18
都是满足要求的，但是我们输出更短的 5 6 7
"""


def mytest(n, l: int):

    f_l = l
    if l % 2 == 0 and n % l == 0:
        f_l = l + 1

    # print(n, f_l)
    # if f_l % 2 == 0:
    #     start = int(n / f_l + 1 - f_l / 2)
    # else:
    #     start = int(n / f_l - (f_l-1) / 2)
    start = int(n / f_l - (f_l-1) / 2)
    # print("start = ", start)
    # print("length =", f_l)
    res_list = [i for i in range(start, start+f_l)]
    # print(res_list)
    return res_list


res = mytest(543792409, 57)
print(len(res))
print(sum(res))

# n,l = map(int,sys.stdin.readline().strip().split())
# print(n, l)
