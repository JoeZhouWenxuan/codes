# 279. 完全平方数
# https://leetcode.cn/problems/perfect-squares/
# 难度：中等
#
# 给你一个整数 n，返回和为 n 的完全平方数的最少数量。
#
# 示例：
# 输入：n = 12    输出：3
# 输入：n = 13    输出：2


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float("inf")] * n

        for square in range(1, int(n ** 0.5) + 1):
            value = square * square
            for total in range(value, n + 1):
                dp[total] = min(dp[total], dp[total - value] + 1)

        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(12))  # 3
    print(s.numSquares(13))  # 2
