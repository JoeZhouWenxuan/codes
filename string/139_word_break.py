# 139. 单词拆分
# https://leetcode.cn/problems/word-break/
# 难度：中等
#
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。
# 如果可以利用字典中出现的一个或多个单词拼接出 s，则返回 true。
# 注意：字典中的单词可以重复使用，不需要使用字典中所有的单词。
#
# 示例：
# 输入：s = "leetcode", wordDict = ["leet","code"]         输出：true
# 输入：s = "applepenapple", wordDict = ["apple","pen"]    输出：true
# 输入：s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]  输出：false
#
# 思路：动态规划。
# dp[i] 表示 s[0..i-1] 能否被拆分。
# 转移：dp[i] = True，若存在 j < i 使得 dp[j] = True 且 s[j..i-1] 在字典中。

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # 空字符串可以被拆分

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]))                          # True
    print(s.wordBreak("applepenapple", ["apple", "pen"]))                     # True
    print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))   # False
