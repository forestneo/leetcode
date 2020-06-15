# -*- coding: utf-8 -*-
# @Time    : 2020/3/23
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 0014_learn.py
# @Software: PyCharm
# @Function: 

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ""
    ret = ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if len(strs[j]) < i+1:
                return ret
            if strs[j][i] != char:
                return ret
        ret = ret + char
    return ret

def longestCommonPrefix_website(strs):
    """python两种让你拍大腿的解法，时间复杂度你想象不到，短小精悍。
    1、利用python的max()和min()，在Python里字符串是可以比较的，
    按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。
    所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
    """
    if not strs: return ""
    s1 = min(strs)
    s2 = max(strs)
    for i, x in enumerate(s1):
        if x != s2[i]:
            return s2[:i]
    return s1


def longestCommonPrefix_website_2(strs):
    """
    利用python的zip函数，把str看成list然后把输入看成二维数组，
    左对齐纵向压缩，然后把每项利用集合去重，之后遍历list中找到元素长度大于1之前的就是公共前缀
    """
    if not strs: return ""
    ss = list(map(set, zip(*strs)))
    res = ""
    for i, x in enumerate(ss):
        x = list(x)
        if len(x) > 1:
            break
        res = res + x[0]
    return res


if __name__ == '__main__':
    strs = ["a", "aaa"]
    print("result: ", longestCommonPrefix(strs))









