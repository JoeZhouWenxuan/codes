# 62. 不同路径
# https://leetcode.cn/problems/unique-paths/
# 难度：中等
#
# 一个机器人位于一个 m x n 网格的左上角，每次只能向下或者向右移动一步。
# 机器人试图达到网格的右下角，问总共有多少条不同的路径？
#
# 示例：
# 输入：m = 3, n = 7    输出：28
# 输入：m = 3, n = 2    输出：3


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [1] * n

        # for _ in range(1, m):
        #     for j in range(1, n):
        #         dp[j] += dp[j - 1]

        # return dp[-1]
        # 一维压缩 DP：
        # dp[j] 表示走到当前行第 j 列的路径数。
        # 第一行每个格子只能一直向右走到达，所以初始化为 1。
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                # dp[j] 原本表示上方格子的路径数，dp[j - 1] 表示左侧格子的路径数。
                # 当前位置只能从上方或左侧过来，所以两者相加。
                dp[j] += dp[j - 1]
        return dp[-1]

    def uniquePaths2D(self, m: int, n: int) -> int:
        # 二维 DP：
        # dp[i][j] 表示从左上角走到第 i 行第 j 列的不同路径数。
        dp = [[0] * n for _ in range(m)]

        # 第一列每个格子只能一直向下走到达，所以路径数都是 1。
        for i in range(m):
            dp[i][0] = 1

        # 第一行每个格子只能一直向右走到达，所以路径数都是 1。
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                # 到达当前位置只能来自上方 dp[i - 1][j] 或左侧 dp[i][j - 1]。
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
    

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 7))  # 28
    print(s.uniquePaths(3, 2))  # 3
    print(s.uniquePaths2D(3, 7))  # 28
    print(s.uniquePaths2D(3, 2))  # 3
