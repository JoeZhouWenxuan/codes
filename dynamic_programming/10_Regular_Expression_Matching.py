# 10. 正则表达式匹配
# https://leetcode.cn/problems/regular-expression-matching/
# 难度：困难
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#
# 示例：
# 输入：s = "aa", p = "a"        输出：False
# 输入：s = "aa", p = "a*"       输出：True
# 输入：s = "ab", p = ".*"       输出：True


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # rows, cols = len(s), len(p)
        # dp = [[False] * (cols + 1) for _ in range(rows + 1)]
        # dp[0][0] = True

        # for j in range(2, cols + 1):
        #     if p[j - 1] == "*":
        #         dp[0][j] = dp[0][j - 2]

        # for i in range(1, rows + 1):
        #     for j in range(1, cols + 1):
        #         if p[j - 1] == "*":
        #             dp[i][j] = dp[i][j - 2]
        #             if p[j - 2] == "." or p[j - 2] == s[i - 1]:
        #                 dp[i][j] = dp[i][j] or dp[i - 1][j]
        #         elif p[j - 1] == "." or p[j - 1] == s[i - 1]:
        #             dp[i][j] = dp[i - 1][j - 1]

        # return dp[rows][cols]
        m, n = len(s), len(p)
        # dp[i][j] 表示 s 的前 i 个字符 s[:i] 是否能被 p 的前 j 个字符 p[:j] 匹配。
        # i 或 j 为 0 时表示空字符串前缀；最终答案是 dp[m][n]。
        # dp = [[False] * (n + 1) for _ in range(m + 1)]
        # dp[0][0] = True
        # for j in range(2, n+1):
        #     if p[j-1] == '*':
        #         dp[0][j] = dp[0][j-2]

        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if p[j-1] == '*':
        #             dp[i][j] = dp[i][j-2]
        #             if s[i-1] == p[j-2] or p[j-2] == '.':
        #                 dp[i][j] = dp[i][j] or dp[i-1][j]

        #         elif s[i-1] == p[j-1] or p[j-1] == '.':
        #             dp[i][j] = dp[i-1][j-1]

        # return dp[-1][-1]

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]

                


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("aa", "a"))    # False
    print(s.isMatch("aa", "a*"))   # True
    print(s.isMatch("ab", ".*"))   # True
