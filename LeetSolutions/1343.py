# -*- coding: utf-8 -*-
# @Time    : 2020/6/15
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 1343.py
# @Software: PyCharm
# @Function: 


"""
1343. 大小为 K 且平均值大于等于阈值的子数组数目

给你一个整数数组 arr 和两个整数 k 和 threshold 。
请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。



示例 1：
输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。
示例 2：

输入：arr = [1,1,1,1,1], k = 1, threshold = 0
输出：5
示例 3：

输入：arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
输出：6
解释：前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。
示例 4：

输入：arr = [7,7,7,7,7,7,7], k = 7, threshold = 7
输出：1
示例 5：

输入：arr = [4,4,4,4], k = 4, threshold = 1
输出：1

提示：
1 <= arr.length <= 10^5
1 <= arr[i] <= 10^4
1 <= k <= arr.length
0 <= threshold <= 10^4
"""

# 超时
def numOfSubarrays(arr, k, threshold):
    ret = 0
    for i in range(len(arr)-k+1):
        print(arr[i:i + k])
        if sum(arr[i:i+k]) >= threshold*k:
            ret += 1
    return ret


def numOfSubarrays_ok(arr, k, threshold):
    ret = 0
    start = 0
    arr_sum = sum(arr[start:start+k])

    if arr_sum >= k * threshold:
        ret += 1
    # print("initial ret = ", ret)
    for i in range(len(arr) - k):
        arr_sum = arr_sum - arr[start]
        start += 1
        arr_sum = arr_sum + arr[start+k-1]
        if arr_sum >= k * threshold:
            ret += 1

    return ret


if __name__ == '__main__':
    # arr = [2,2,2,2,5,5,5,8]
    # k = 1
    arr = [1,1,1,1]
    k = 1
    threshold = 1
    print(numOfSubarrays_new(arr, k, threshold))











