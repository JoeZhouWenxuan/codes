# 516. 最长回文子序列
# https://leetcode.cn/problems/longest-palindromic-subsequence/
# 难度：中等
#
# 给你一个字符串 s，找出其中最长的回文子序列，并返回该序列的长度。
#
# 示例：
# 输入：s = "bbbab"    输出：4
# 输入：s = "cbbd"     输出：2


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindromeSubseq("bbbab"))  # 4
    print(s.longestPalindromeSubseq("cbbd"))   # 2
