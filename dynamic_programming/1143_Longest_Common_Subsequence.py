# 1143. 最长公共子序列
# https://leetcode.cn/problems/longest-common-subsequence/
# 难度：中等
#
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
#
# 示例：
# 输入：text1 = "abcde", text2 = "ace"    输出：3
# 输入：text1 = "abc", text2 = "abc"      输出：3


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        # dp[i][j] 表示 text1 前 i 个字符和 text2 前 j 个字符的最长公共子序列长度。
        # 多开一行一列作为空字符串边界：dp[0][j] 和 dp[i][0] 都为 0。
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[rows][cols]
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        dp = [[0]* (cols + 1) for _ in range(rows + 1)]
        for i in range(1, rows):
            for j in range(1, cols):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        # 一维压缩：dp[j] 表示当前遍历到 text1 前 i 个字符时，
        # 它和 text2 前 j 个字符的最长公共子序列长度。
        dp = [0] * (cols + 1)

        for i in range(1, rows + 1):
            # prev 保存二维状态中的 dp[i - 1][j - 1]，temp 保存更新前的 dp[i - 1][j]。
            prev = 0
            for j in range(1, cols + 1):
                temp = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        return dp[cols]


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonSubsequence("abcde", "ace"))  # 3
    print(s.longestCommonSubsequence("abc", "abc"))    # 3
