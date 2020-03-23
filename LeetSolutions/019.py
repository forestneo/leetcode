# -*- coding: utf-8 -*-
# @Time    : 2020/3/23
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 019.py
# @Software: PyCharm
# @Function: 

"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def print_ln(ln: ListNode):
    while ln:
        print(str(ln.val) + ", ", end="")
        ln = ln.next


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy_head = ListNode(-1)
    dummy_head.next = head

    length = 0
    temp_node = head
    while temp_node:
        length += 1
        temp_node = temp_node.next

    index = length - n
    temp_node = dummy_head
    for i in range(index):
        temp_node = temp_node.next
    print(temp_node.val)
    next_node = temp_node.next
    temp_node.next = next_node.next
    return dummy_head.next


def removeNthFromEnd_website(self, head: ListNode, n: int) -> ListNode:
    global count
    if head is None:
        count = 0
        return None
    head.next = self.removeNthFromEnd(head.next, n)
    count += 1
    return head.next if n == count else head


if __name__ == '__main__':
    a = ListNode(1)
    # b = ListNode(2)
    # c = ListNode(3)
    # d = ListNode(4)
    # e = ListNode(5)
    # a.next = b
    # b.next = c
    # c.next = d
    # d.next = e
    head = a

    lst = removeNthFromEnd(head, 1)
    print_ln(lst)

    pass


