# -*- coding: utf-8 -*-
# @Time    : 2020/3/23
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 0021_todo.py
# @Software: PyCharm
# @Function: 

"""
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists_others(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 and l2:
        if l1.val > l2.val: l1, l2 = l2, l1
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1 or l2


def mergeTwoLists_others2(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    move = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            move.next = l1
            l1 = l1.next
        else:
            move.next = l2
            l2 = l2.next
        move = move.next
    move.next = l1 if l1 else l2
    return dummy.next


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    dummy_head = ListNode(0)
    current_node = dummy_head
    while l1 and l2:
        if l1.val < l2.val:
            new_node = ListNode(l1.val)
            l1 = l1.next
            current_node.next = new_node
            current_node = current_node.next
        else:
            new_node = ListNode(l2.val)
            l2 = l2.next
            current_node.next = new_node
            current_node = current_node.next
    if l1 is None and l2 is None:
        return dummy_head.next
    ls = l1 if l2 is None else l2
    while ls:
        new_node = ListNode(ls.val)
        current_node.next = new_node
        current_node = current_node.next
        ls = ls.next
    return dummy_head.next


def print_ln(ln: ListNode):
    while ln:
        print(str(ln.val) + ", ", end="")
        ln = ln.next





if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(4)
    a.next=b
    b.next=c
    l1 = a

    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(4)
    a.next = b
    b.next = c
    l2 = a

    ls = mergeTwoLists(l1, l2)
    print_ln(ls)