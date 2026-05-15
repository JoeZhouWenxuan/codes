# 221. 最大正方形
# https://leetcode.cn/problems/maximal-square/
# 难度：中等
#
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
#
# 示例：
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]    输出：4
# 输入：matrix = [["0","1"],["1","0"]]                                                                            输出：1

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 思路：
        # 1. dp[i][j] 表示“以 matrix[i - 1][j - 1] 为右下角的最大正方形边长”。
        # 2. 如果当前位置是 '0'，那么边长一定为 0。
        # 3. 如果当前位置是 '1'，它能扩成多大的正方形，取决于：
        #    上、左、左上这三个位置能形成的最大正方形边长的最小值，再加 1。
        # 4. 转移方程：
        #    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        if not matrix or not matrix[0]:
            return 0

        # rows, cols = len(matrix), len(matrix[0])
        # dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        # max_side = 0

        # for i in range(1, rows + 1):
        #     for j in range(1, cols + 1):
        #         if matrix[i - 1][j - 1] == "1":
        #             dp[i][j] = min(
        #                 dp[i - 1][j],
        #                 dp[i][j - 1],
        #                 dp[i - 1][j - 1],
        #             ) + 1
        #             max_side = max(max_side, dp[i][j])

        # return max_side * max_side
        max_side = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side

if __name__ == "__main__":
    s = Solution()
    print(
        s.maximalSquare(
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ]
        )
    )  # 4
    print(s.maximalSquare([["0", "1"], ["1", "0"]]))  # 1
