# -*- coding: utf-8 -*-
# @Time    : 2020/6/20
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 004.py
# @Software: PyCharm
# @Function: 

"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

给定 target = 5，返回 true。
给定 target = 20，返回 false。
"""


def findNumberIn2DArray(matrix, target: int) -> bool:
    if len(matrix) < 1 or len(matrix[0]) < 1 or matrix[0][0] > target or matrix[-1][-1] < target:
        return False
    for i in range(len(matrix)):
        if matrix[i][0] <= target and target in matrix[i]:
            return True
    return False


def find_accelerate(matrix, target: int):
    if len(matrix) < 1 or len(matrix[0]) < 1:
        return False
    row, col = len(matrix), len(matrix[0])
    for i in range(row-1, -1, -1):
        if matrix[i][0] > target:
            # 这一行无需查找
            continue
        # 查找这一行
        print("finding ", i)
        for item in matrix[i]:
            if item == target:
                return True
            if item > target:
                break
    return False



if __name__ == '__main__':
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    # matrix = [[]]
    target = 20
    print(find_accelerate(matrix, target))
