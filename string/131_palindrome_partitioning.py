# 131. 分割回文串
# https://leetcode.cn/problems/palindrome-partitioning/
# 难度：中等
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。
# 返回 s 所有可能的分割方案。
#
# 示例：
# 输入：s = "aab"  输出：[["a","a","b"],["aa","b"]]
# 输入：s = "a"    输出：[["a"]]
#
# 思路：回溯 + 动态规划预处理回文判断。
# dp[i][j] 表示 s[i..j] 是否是回文串，避免回溯时重复判断。

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        # 预处理：dp[i][j] = s[i..j] 是否是回文
        dp = [[True] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

        ans = []
        path = []

        def backtrack(start):
            if start == n:
                ans.append(path[:])
                return
            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))  # [['a', 'a', 'b'], ['aa', 'b']]
    print(s.partition("a"))    # [['a']]
