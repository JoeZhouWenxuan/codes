# 64. 最小路径和
# https://leetcode.cn/problems/minimum-path-sum/
# 难度：中等
#
# 给定一个包含非负整数的 m x n 网格 grid，请找出一条从左上角到右下角的路径，
# 使得路径上的数字总和为最小。每次只能向下或者向右移动一步。
#
# 示例：
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]    输出：7
# 输入：grid = [[1,2,3],[4,5,6]]            输出：12

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # rows, cols = len(grid), len(grid[0])
        # dp = [0] * cols

        # for i in range(rows):
        #     for j in range(cols):
        #         if i == 0 and j == 0:
        #             dp[j] = grid[i][j]
        #         elif i == 0:
        #             dp[j] = dp[j - 1] + grid[i][j]
        #         elif j == 0:
        #             dp[j] = dp[j] + grid[i][j]
        #         else:
        #             dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        # return dp[-1]
        m, n = len(grid), len(grid[0])
        dp = [0] * n 
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif i == 0:
                    dp[j] = dp[j-1] + grid[i][j]
                elif j == 0:
                    dp[j] += dp[j]  + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # 7
    print(s.minPathSum([[1, 2, 3], [4, 5, 6]]))             # 12
