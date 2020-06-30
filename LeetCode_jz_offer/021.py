# -*- coding: utf-8 -*-
# @Time    : 2020/6/30
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 021.py
# @Software: PyCharm
# @Function: 

"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4]

注：[3,1,2,4] 也是正确的答案之一。
"""


def exchange(self, nums):
    pre, post = 0, len(nums) - 1
    while (pre < post):
        if nums[pre] % 2 == 0:
            nums[pre], nums[post] = nums[post], nums[pre]
            post -= 1
        else:
            pre += 1
    # print(nums)
    return nums