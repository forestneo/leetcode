# -*- coding: utf-8 -*-
# @Time    : 2020/6/19
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 1414.py
# @Software: PyCharm
# @Function: 


def findMinFibonacciNumbers(k: int):
    fib_arr = [1] * 45
    for i in range(2, len(fib_arr)):
        fib_arr[i] = fib_arr[i-1] + fib_arr[i-2]
    print(fib_arr)

    res = 0
    fib_index = len(fib_arr) - 1
    while k > 0:
        if k >= fib_arr[fib_index]:
            cnt = k // fib_arr[fib_index]
            print("find item: ", fib_arr[fib_index], ", cnt = ", cnt)
            k = k - cnt * fib_arr[fib_index]
            res += cnt
        fib_index = fib_index - 1
    return res



if __name__ == '__main__':
    k = 10
    res = tian_sol(k)
    print(res)
