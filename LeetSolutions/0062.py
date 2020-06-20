# -*- coding: utf-8 -*-
# @Time    : 2020/6/18
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 0062.py
# @Software: PyCharm
# @Function: 




def uniquePaths(m, n):
    def calculate_c(m, n):
        top = 1
        for i in range(1, n + 1):
            top *= m
            m -= 1
        bottom = 1
        for i in range(1, n + 1):
            bottom *= i
        return top // bottom

    if m < n:
        m, n = n, m
    # calculate C_m^n
    res = calculate_c(m+n-2, n-1)
    return res


def uniquePaths_dp(m, n):
    if m == 1 or n == 1:
        return 1
    return uniquePaths_dp(m-1, n) + uniquePaths_dp(m, n - 1)


def uniquePaths_dp_new(m, n):
    matrix = [[1 for i in range(n)] for i in range(m)]
    for i in range(n):
        matrix[0][i] = 1
    for i in range(m):
        matrix[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            print(i, j)
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    return matrix[m-1][n-1]


def uniquePath_dp_todo(m, n):
    dp = [([1] * n) for k in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]


if __name__ == '__main__':
    m = 3
    n = 3
    res = uniquePath_dp_todo(m, n)
    print(res)
    # pass