# 72. 编辑距离
# https://leetcode.cn/problems/edit-distance/
# 难度：困难
#
# 给你两个单词 word1 和 word2，请返回将 word1 转换成 word2 所使用的最少操作数。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符
#
# 示例：
# 输入：word1 = "horse", word2 = "ros"      输出：3
# 输入：word1 = "intention", word2 = "execution"    输出：5


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # rows, cols = len(word1), len(word2)
        # dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        # for i in range(rows + 1):
        #     dp[i][0] = i
        # for j in range(cols + 1):
        #     dp[0][j] = j

        # for i in range(1, rows + 1):
        #     for j in range(1, cols + 1):
        #         if word1[i - 1] == word2[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1]
        #         else:
        #             dp[i][j] = min(
        #                 dp[i - 1][j] + 1,
        #                 dp[i][j - 1] + 1,
        #                 dp[i - 1][j - 1] + 1,
        #             )

        # return dp[rows][cols]
    
        m, n = len(word1), len(word2)
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[m][n]


if __name__ == "__main__":
    s = Solution()
    print(s.minDistance("horse", "ros"))            # 3
    print(s.minDistance("intention", "execution"))  # 5
