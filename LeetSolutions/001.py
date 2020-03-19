# -*- coding: utf-8 -*-
# @Time    : 2020/3/15
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 001.py
# @Software: PyCharm
# @Function:


def twoSum_v1(nums: list, target):
    for i in range(len(nums) - 1):
        if target - nums[i] in nums[i + 1:]:
            return i, nums[i + 1:].index(target - nums[i]) + i + 1


def twoSum_v2(nums:list, target):
    sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
    print(sorted_id)



if __name__ == '__main__':
    a = [3,3,4,1]
    b = 6
    # print(twoSum_v1(a, b))
    twoSum_v2(a, b)

    students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    a = sorted(students, key=lambda s: s[2])
    print(a)
