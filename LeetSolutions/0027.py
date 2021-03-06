# -*- coding: utf-8 -*-
# @Time    : 2020/3/28
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 0027.py
# @Software: PyCharm
# @Function: 

"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,1,2,2,3,0,4,2], val = 2,
函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。
你不需要考虑数组中超出新长度后面的元素。
"""


def removeElement(nums: list, val: int):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    if len(nums) == 0 or (len(nums) == 1 and nums[0] == val):
        return 0
    i, j = 0, len(nums)-1
    while i <= j:
        if nums[i] != val:
            i += 1
            continue
        if nums[j] == val:
            j -= 1
            continue
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return i


if __name__ == '__main__':
    # nums = [0, 1, 2, 2, 3, 0, 4, 2]
    nums = [5,5,5]
    val = 5
    length = removeElement(nums, val)
    print("length = ", length)
    for i in range(length):
        print(nums[i])
    pass