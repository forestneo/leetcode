# -*- coding: utf-8 -*-
# @Time    : 2020/6/15
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 1144.py
# @Software: PyCharm
# @Function: 

"""
给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。

如果符合下列情况之一，则数组 A 就是 锯齿数组：
每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
返回将数组 nums 转换为锯齿数组所需的最小操作次数。

示例 1：
输入：nums = [1,2,3]
输出：2
解释：我们可以把 2 递减到 0，或把 3 递减到 1。

示例 2：
输入：nums = [9,6,1,6,2]
输出：4
"""


def my_solution_ok(nums):
    ret = 0
    ret_1 = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            # 奇数
            left = 1001 if i-1 < 0 else nums[i-1]
            right = 1001 if i+1 >= len(nums) else nums[i+1]
            print(left, nums[i], right)
            move = nums[i] - min(left, right) + 1 if nums[i] >= min(left, right) else 0
            print("move = ", move)
            ret_1 = ret_1 + move
            print("ret_1 = ", ret_1)
    ret = ret_1

    print("\n\n")
    ret_2 = 0
    for i in range(len(nums)):
        if i % 2 == 1:
            # 偶数
            print("i = ", i)
            left = 1001 if i-1 < 0 else nums[i-1]
            right = 1001 if i+1 >= len(nums) else nums[i+1]
            print(left, nums[i], right)
            move = nums[i] - min(left, right) + 1 if nums[i] >= min(left, right) else 0
            print("move = ", move)
            ret_2 = ret_2 + move
            print("ret_2 = ", ret_2)

    ret = min(ret_1, ret_2)
    return ret

def my_solution_short(nums):
    ret_1, ret_2 = 0, 0
    for i in range(len(nums)):
        left = 1001 if i - 1 < 0 else nums[i - 1]
        right = 1001 if i + 1 >= len(nums) else nums[i + 1]
        print(left, nums[i], right)
        move = nums[i] - min(left, right) + 1 if nums[i] >= min(left, right) else 0
        if i % 2 == 0:
            ret_1 = ret_1 + move
        else:
            ret_2 = ret_2 + move
    return min(ret_1, ret_2)


if __name__ == '__main__':
    # nums = [9,6,1,6,2]
    # nums = [1,2,3]
    nums = [10,4,4,10,10,6,2,3]
    print(my_solution_ok(nums))
    pass







