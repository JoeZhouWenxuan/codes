# 139. 单词拆分
# https://leetcode.cn/problems/word-break/
# 难度：中等
#
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。
# 请你判断是否可以利用字典中出现的单词拼接出 s。
#
# 示例：
# 输入：s = "leetcode", wordDict = ["leet","code"]    输出：True
# 输入：s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]    输出：False

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # words = set(wordDict)
        # dp = [False] * (len(s) + 1)
        # dp[0] = True

        # for i in range(1, len(s) + 1):
        #     for j in range(i):
        #         if dp[j] and s[j:i] in words:
        #             dp[i] = True
        #             break

        # return dp[-1]

        words = set(wordDict)
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j: i] in words:
                    dp[i] = True
                    break
        return dp[-1]
    
if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]))                      # True
    print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False
