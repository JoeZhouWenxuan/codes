# 132. 分割回文串 II
# https://leetcode.cn/problems/palindrome-partitioning-ii/
# 难度：困难
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
# 返回符合要求的最少分割次数。
#
# 示例：
# 输入：s = "aab"    输出：1
# 输入：s = "a"      输出：0


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        dp = [0] * n
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
                continue
            dp[i] = i
            for j in range(i):
                if is_pal[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.minCut("aab"))  # 1
    print(s.minCut("a"))    # 0
