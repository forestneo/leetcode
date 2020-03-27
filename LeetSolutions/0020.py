# -*- coding: utf-8 -*-
# @Time    : 2020/3/24
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 0020.py
# @Software: PyCharm
# @Function:

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    def isPair(a, b):
        if a == '(' and b == ')':
            return True
        elif a == '{' and b == '}':
            return True
        elif a == '[' and b == ']':
            return True
        else:
            return False

    stack = []
    for item in s:
        if item in ['(', '{', '[']:
            stack.append(item)
        else:
            if len(stack) == 0:
                return False
            char = stack.pop()
            if not isPair(char, item):
                return False
    if len(stack) == 0:
        return True
    return False


def isValid_internet(s: str) -> bool:
    dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
    stack = ['?']
    for c in s:
        print("processing: ", c)
        if c in dic:
            stack.append(c)
            print("c = ", c, " stack = ", stack)
        elif dic[stack.pop()] != c:
            return False
    return len(stack) == 1


if __name__ == '__main__':
    str = "{[]}"
    print(isValid_internet(str))