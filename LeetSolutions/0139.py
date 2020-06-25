# -*- coding: utf-8 -*-
# @Time    : 2020/6/25
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 0139.py
# @Software: PyCharm
# @Function: 
"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""


# 超时
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        if s == "":
            return True
        for i in range(len(s)):
            current_word = s[0:i+1]
            # print("current word:", current_word)
            if current_word in wordDict:
                # print("recurrence: ", s[i+1:])
                if self.wordBreak(s[i+1:], wordDict):
                    return True
        return False

    # 通过
    def wordBreak_new(self, s, wordDict):
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)+1):
            for j in range(i):
                word = s[j:i]
                if dp[j] and word in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    # s = "catanddog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    print(sol.wordBreak_new(s, wordDict))
