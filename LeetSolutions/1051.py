# -*- coding: utf-8 -*-
# @Time    : 2020/6/18
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 1051.py
# @Software: PyCharm
# @Function: 

"""
1051. 高度检查器
学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。
请你返回能让所有学生以 非递减 高度排列的最小必要移动人数。
注意，当一组学生被选中时，他们之间可以以任何可能的方式重新排序，而未被选中的学生应该保持不动。

示例：

输入：heights = [1,1,4,2,1,3]
输出：3
解释：
当前数组：[1,1,4,2,1,3]
目标数组：[1,1,1,2,3,4]
在下标 2 处（从 0 开始计数）出现 4 vs 1 ，所以我们必须移动这名学生。
在下标 4 处（从 0 开始计数）出现 1 vs 3 ，所以我们必须移动这名学生。
在下标 5 处（从 0 开始计数）出现 3 vs 4 ，所以我们必须移动这名学生。
示例 2：

输入：heights = [5,1,2,3,4]
输出：5
示例 3：

输入：heights = [1,2,3,4,5]
输出：0


提示：
1 <= heights.length <= 100
1 <= heights[i] <= 100
"""


def heightChecker_ok(heights: list):
    sort_heights = sorted(heights)
    print(sort_heights)
    ret = 0
    for i in range(len(heights)):
        if heights[i] != sort_heights[i]:
            ret += 1
    return ret


"""理论上应该更快，测试结果却更慢"""
def heightChecker_new(heights):
    arr = [0 for _ in range(101)]
    for height in heights:
        arr[height] += 1
    ret = 0
    heights_index = 0
    for arr_index in range(len(arr)):
        value, count = arr_index, arr[arr_index]
        while count > 0:
            if heights[heights_index] != value:
                ret += 1
            heights_index += 1
            count = count - 1
    return ret


if __name__ == '__main__':
    heights = [1, 1, 4, 2, 1, 3]
    ret = heightChecker_new(heights)
    print(ret)



