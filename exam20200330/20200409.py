# -*- coding: utf-8 -*-
# @Time    : 2020/4/10
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 20200410.py
# @Software: PyCharm
# @Function: 


def quick_sort(arr, start, end):
    if start >= end:
        return
    left = start
    right = end
    mid = arr[left]
    while left < right:
        while left < right and arr[right] >= mid:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] < mid:
            left += 1
        arr[right] = arr[left]
    arr[left] = mid
    quick_sort(arr, start, left - 1)
    quick_sort(arr, left + 1, end)


def my_find_min_k(arr, k):
    if len(arr) < k:
        raise Exception("the input is wrong")
    quick_sort(arr, 0, len(arr)-1)
    return arr[k-1]


if __name__ == '__main__':
    input_arr = [6, 3, 2, 9, 9, 7]
    k = 2
    print(my_find_min_k(input_arr, k))