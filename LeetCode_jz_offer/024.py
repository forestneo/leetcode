# -*- coding: utf-8 -*-
# @Time    : 2020/6/30
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 024.py
# @Software: PyCharm
# @Function: 
"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

限制：
0 <= 节点个数 <= 5000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        a = ListNode(-1)
        b = ListNode(-1)
        c = head
        a.next = b
        b.next = c
        while c:
            b.next = a
            a, b, c = b, c, c.next
        b.next = a
        head.next = None
        return b



if __name__ == '__main__':
    pass