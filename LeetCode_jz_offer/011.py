# -*- coding: utf-8 -*-
# @Time    : 2020/6/22
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 011.py
# @Software: PyCharm
# @Function: 

"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：
输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
"""


def slow(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return numbers[i]
    return numbers[0]


def divide(numbers):
    i, j = 0, len(numbers) - 1

    while i + 1 < j:
        print(numbers[i:j+1])
        m = (i + j) // 2
        if numbers[i] <= numbers[m] <= numbers[j]:
            j = j - 1
        elif numbers[m] > numbers[j]:
            i = m
        else:
            j = m
    # print(i, j)
    return min(numbers[i], numbers[j])


if __name__ == '__main__':
    # numbers = [3, 4, 1]
    # numbers = [3, 3, 1, 3]
    numbers = [3, 4, 5, 1, 2]
    # print(slow(numbers))
    print(divide(numbers))
    pass