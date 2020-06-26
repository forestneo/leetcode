# -*- coding: utf-8 -*-
# @Time    : 2020/6/22
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 012.py
# @Software: PyCharm

"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
"""

import numpy as np

class Solution_old:
    def find_path(self, i, j, visited, board, left_str):
        if len(left_str) == 0:
            return True

        next_char = left_str[0]
        left_str = left_str[1:]
        # print("next_char = ", next_char)

        row, col = len(visited), len(board[0])

        res = [False, False, False, False]

        # up
        index_i, index_j = i-1, j
        if 0 <= index_i < row and 0 <= index_j < col and visited[index_i][index_j] == False and board[index_i][index_j] == next_char:
            # print("up")
            # copy a new visited matrix
            new_visited = visited.copy()
            new_visited[index_i][index_j] = True
            up_res = self.find_path(i=index_i, j=index_j, visited=new_visited, board=board, left_str=left_str)
            res[0] = up_res

        index_i, index_j = i + 1, j
        if 0 <= index_i < row and 0 <= index_j < col and visited[index_i][index_j] == False and board[index_i][index_j] == next_char:
            # print("down")
            # copy a new visited matrix
            new_visited = visited.copy()
            new_visited[index_i][index_j] = True
            up_res = self.find_path(i=index_i, j=index_j, visited=new_visited, board=board, left_str=left_str)
            res[1] = up_res

        index_i, index_j = i, j-1
        if 0 <= index_i < row and 0 <= index_j < col and visited[index_i][index_j] == False and board[index_i][index_j] == next_char:
            # print("left")
            # copy a new visited matrix
            new_visited = visited.copy()
            new_visited[index_i][index_j] = True
            up_res = self.find_path(i=index_i, j=index_j, visited=new_visited, board=board, left_str=left_str)
            res[2] = up_res

        index_i, index_j = i, j+1
        if 0 <= index_i < row and 0 <= index_j < col and visited[index_i][index_j] == False and board[index_i][index_j] == next_char:
            # print("right")
            # copy a new visited matrix
            new_visited = visited.copy()
            new_visited[index_i][index_j] = True
            up_res = self.find_path(i=index_i, j=index_j, visited=new_visited, board=board, left_str=left_str)
            res[3] = up_res
        if True in res:
            return True
        return False


    def exist(self, board, word: str):
        if len(board) == 0 or len(board[0]) == 0:
            return False

        row, col = len(board), len(board[0])

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    visited = np.zeros(shape=(row,col), dtype=int)
                    visited[i][j] = 1
                    # start find word
                    print("find start flag: ", i, j)
                    # print('visited = ', visited)

                    left_str = word[1:]
                    res = self.find_path(i, j, visited, board, left_str)
                    # print("find start flag: ", i, j, ", result = ", res)
                    if res:
                        return True
                    print()
        return False


class Solution_new:

    def exist(self, board, word: str):
        def dfs(next_position, left_word, visited_flag):
            if left_word == "":
                return True
            i, j = next_position[0], next_position[1]
            if not (0 <= i < row and 0 <= j < col and (visited_flag[i][j] == 0) and left_word[0] == board[i][j]):
                return False

            # 找到了当前节点
            visited_flag[i][j] = True
            new_left_word = left_word[1:]
            if dfs([i-1, j], new_left_word, visited_flag):
                return True
            elif dfs([i+1, j], new_left_word, visited_flag):
                return True
            elif dfs([i, j-1], new_left_word, visited_flag):
                return True
            elif dfs([i, j+1], new_left_word, visited_flag):
                return True
            else:
                visited_flag[i][j] = False
                return False

        if len(board) == 0 or len(board[0]) == 0:
            return False
        if word == "":
            return True

        row, col = len(board), len(board[0])
        visited_flag = np.zeros(shape=(row, col), dtype=bool)

        for i in range(row):
            for j in range(col):
                result = dfs(next_position=[i,j], left_word=word, visited_flag=visited_flag)
                if result:
                    return True
        return False


class Solution:
    def exist(self, board, word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False



if __name__ == '__main__':
    board = [["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","b"]]
    word = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCCED"

    solution = Solution_new()
    res = solution.exist(board, word)
    print(res)