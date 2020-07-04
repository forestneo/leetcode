# -*- coding: utf-8 -*-
# @Time    : 2020/7/5
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 029.py
# @Software: PyCharm
# @Function: 
"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：
0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
"""

class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        m, n = len(matrix), len(matrix[0])
        flag = [[0 for i in range (n)] for i in range(m)]

        # current pos
        cur_pos = [0, 0]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # current direction
        cur_dir_index = 0
        result = [matrix[cur_pos[0]][cur_pos[1]]]
        flag[0][0]=1

        while len(result) < m * n:
            # get next item
            next_pos = [cur_pos[0] + direction[cur_dir_index][0], cur_pos[1] + direction[cur_dir_index][1]]
            if 0 <= next_pos[0] < m and 0 <= next_pos[1] < n and flag[next_pos[0]][next_pos[1]] == 0:
                # the direction is ok
                cur_pos = next_pos
                add_item = matrix[cur_pos[0]][cur_pos[1]]
                result.append(add_item)
                flag[cur_pos[0]][cur_pos[1]] = 1
            else:
                # the direction is wrong
                cur_dir_index = (cur_dir_index+1) % 4
        return result


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    sol = Solution()
    res = sol.spiralOrder(matrix)
    print(res)
