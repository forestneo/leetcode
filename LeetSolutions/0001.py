# -*- coding: utf-8 -*-
# @Time    : 2020/3/15
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 0001.py
# @Software: PyCharm
# @Function:
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

def twoSum_v1(nums: list, target):
    for i in range(len(nums) - 1):
        if target - nums[i] in nums[i + 1:]:
            return i, nums[i + 1:].index(target - nums[i]) + i + 1


def twoSum_v2(nums:list, target):
    b = [1,2,4,3]
    # sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
    sorted_id = sorted(b, key=lambda k: nums[k])
    print(sorted_id)


def twoSum_internet(nums, target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]

if __name__ == '__main__':
    a = [3,3,3,2,4]
    b = 6
    twoSum_v2(a, b)
    # print(twoSum_internet(a, b))

