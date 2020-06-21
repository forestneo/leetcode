# -*- coding: utf-8 -*-
# @Time    : 2020/6/21
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 007.py
# @Software: PyCharm
# @Function: 

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(self, preorder, inorder) -> TreeNode:
    if len(preorder) < 1:
        return None
    if len(preorder) == 1:
        return TreeNode(preorder[0])

    value = preorder[0]
    pos = inorder.index(value)
    left_length = pos
    right_length = len(inorder) - left_length - 1

    # print("left_length = ", left_length)
    # print("right_length = ", right_length)

    preorder_left = preorder[1:1 + left_length]
    preorder_right = preorder[1 + left_length: len(preorder) + 1]

    inorder_left = inorder[0:pos]
    inorder_right = inorder[pos + 1:len(preorder) + 1]

    # print("left tree:  ", preorder_left, inorder_left)
    # print("right tree: ", preorder_right, inorder_right)

    middle_node = TreeNode(preorder[0])
    middle_node.left = self.buildTree(preorder_left, inorder_left)
    middle_node.right = self.buildTree(preorder_right, inorder_right)
    return middle_node


if __name__ == '__main__':
    pass