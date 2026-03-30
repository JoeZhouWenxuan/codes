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
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 7))  # 28
    print(s.uniquePaths(3, 2))  # 3
