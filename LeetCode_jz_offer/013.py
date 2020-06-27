# -*- coding: utf-8 -*-
# @Time    : 2020/6/27
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 013.py
# @Software: PyCharm
# @Function: 

"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int):

        import numpy as np

        # def isEffective(pos_i, pos_j):
        #     return 0 <= pos_i < m and 0 <= pos_j < n and visited_flag[pos_i][pos_j] == 0 and sum([int(item) for item in (str(pos_i) + str(pos_j))]) <= k

        def dfs(i, j):
            # print("now visite ", i, j)
            if 0 <= i < m and 0 <= j < n and visited_flag[i][j] == 0 and sum([int(item) for item in (str(i) + str(j))]) <= k:
                # print("visited :", i, j)
                visited_flag[i][j] = 1
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)

        visited_flag = np.zeros(shape=(m, n), dtype=int)
        dfs(0, 0)
        return int(np.sum(visited_flag))


if __name__ == '__main__':
    sol = Solution()
    # m, n, k = 2, 3, 1
    m, n, k = 5, 6, 9
    res = sol.movingCount(m, n, k)
    print("solution = ", res)














